import datetime
import pymysql
import re
import numpy as np
import gzip
import urllib.request


class parse_nglog:
    def __init__(self,datestart,dateend,table_name,parse_re,**kwargs):
        '''
        :param datestart:日志数据起始日期 （格式为：'2019-05-01'）
        :param dateend: 日志数据结束日期（格式为：'2019-05-01'）
        :param table_name: 数据库新建表名（会加上起止日期）
        :param parse_re: url的正则表达式，如需解析id需带括号，例如：’/s-view-(\d+)‘
        :param kwargs: type 为 pv 则解析流量事件，为 click 则解析点击事件； parse_id 为True 流量事件url会解析为id，为False 不会解析，默认为False
        '''
        self.datestart = datestart
        self.dateend = dateend
        self.table_name = kwargs['type'] + '_' + table_name + datestart + '_' + dateend
        self.parse_re = parse_re
        self.url_parse_kw = kwargs
        self.log_date_list = self.create_date_list()
        self.conn = self.dbconn_nglog_analyse()
        self.cur = self.conn.cursor()


    def create_date_list(self):
        '''建立日期列表，生成的日志列表会比输入日期大一天，因为日志生成的是前一天的数据'''
        # 转为日期格式
        datestart = datetime.datetime.strptime(self.datestart, '%Y-%m-%d')
        dateend = datetime.datetime.strptime(self.dateend, '%Y-%m-%d')

        date_list = []
        while datestart <= dateend:
            # 日期叠加一天
            datestart += datetime.timedelta(days=+1)
            # 日期转字符串存入列表
            date_list.append(datestart.strftime('%Y%m%d'))
        return date_list


    def log_name_iter(self):
        '''需要读取数据的日志文件名迭代器'''
        for log_date in self.log_date_list:
            log_name = "/mnt/log/trace-web.tuliu.com/access_" + log_date + ".log.gz"
            yield log_name


    def logtime_format(self,logtime):
        '''将nginx日志中的日期转化为便于数据库存储的日期格式'''
        en_mon = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        num_mon = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']



        pattern_time = re.compile(r'(\d+)/(\w+)/(\d+):(\d+):(\d+):(\d+)')
        m_time = pattern_time.search(logtime)
        year = m_time.group(3)
        mon = m_time.group(2)
        for i in np.arange(12):
            if mon == en_mon[i]:
                mon = num_mon[i]
        day = m_time.group(1)
        h = m_time.group(4)
        m = m_time.group(5)
        s = m_time.group(6)
        time = year + '-' + mon + '-' + day + ' ' + h + ':' + m + ':' + s + ''
        return time


    def judge_baiduspider(self,uag):
        '''判断uag是否包含百度爬虫，包含返回True，不包含返回False'''
        pattern = re.compile(r'baiduspider')
        m = pattern.search(uag)
        if m == None:
            result = False
        else:
            result = True
        return result


    def judge_event_id(self,url):
        '''判断url是否包含event_id，包含返回True，不包含返回False'''
        pattern = re.compile(r'.*event_id.*')
        m = pattern.search(url)
        if m == None:
            result = False
        elif m != None:
            result = True
        else:
            result = None
        return result


    def judge_url_re(self,url):
        '''判断是否符合url正则表达式，符合返回True，不符合返回False'''
        pattern = re.compile(r'.*'+str(self.parse_re)+'.*')
        m=pattern.search(url)
        if m != None:
            result = True
        else:
            result = False
        return result


    def judge_event_re(self,event):
        '''判断是否符合点击事件的正则表达式，符合返回True，不符合返回False'''
        pattern = re.compile(r'.*'+str(self.parse_re)+'.*')
        m=pattern.search(event)
        if m != None:
            result = True
        else:
            result = False
        return result


    def parse_url_id(self,url):
        '''解析url中的id，并提取出来（仅为parse=True时提取）'''
        if self.url_parse_kw.get("parse_id", None) is None: # 如果parse_id参数未填写
            url_id = url
        elif self.url_parse_kw['parse_id'] == True:
            pattern = re.compile(r'.*' + str(self.parse_re) + '.*')
            m = pattern.search(url)
            url_id = m.group(1)
        elif self.url_parse_kw['parse_id'] == False:
            url_id = url
        else:
            url_id = url
        return url_id


    def dbconn_nglog_analyse(self):
        '''日志分析数据库连接'''
        dbconn = pymysql.connect(
            host="******",
            user="******",
            password="******",
            db="******",
            port=3306,
            charset='utf8'
        )
        return dbconn


    def close_dbconn(self):
        '''关闭数据库连接、游标'''
        self.conn.close()
        self.cur.close()


    def create_table(self):
        '''数据库建表,点击事件比流量事件多一个event字段'''
        if self.url_parse_kw['type'] == 'pv':
            sql_drop='drop table if exists `%s`'%(self.table_name)
            sql_create='''
                CREATE TABLE `%s` (
              `id` int(20) unsigned NOT NULL AUTO_INCREMENT,
              `time` datetime DEFAULT NULL COMMENT '访问时间',
              `ip` varchar(22) DEFAULT NULL COMMENT 'ip地址',
              `status` int(5) DEFAULT '0' COMMENT '状态码',
              `lgt` char(1) DEFAULT '' COMMENT '页面事件类型（1为页面初始化）',
              `dm` varchar(1000) DEFAULT '' COMMENT '访问域名',
              `rf` varchar(2000) DEFAULT '' COMMENT '上一页来源地址',
              `url` varchar(2000) DEFAULT '' COMMENT '当前访问URL',
              `tt` varchar(1000) DEFAULT '' COMMENT '访问地址的标题',
              `rlt` varchar(500) DEFAULT '' COMMENT '用户屏幕(高度+宽度)',
              `dt` int(10) DEFAULT '0' COMMENT '目标设备或缓冲器上的调色板的比特深度',
              `lu` char(20) DEFAULT '' COMMENT '客户端语言设置',
              `bs` varchar(100) DEFAULT '' COMMENT '浏览器类型',
              `os` varchar(50) DEFAULT '' COMMENT '客户端系统类型',
              `ct` varchar(50) DEFAULT '' COMMENT '客户端访问手机类型',
              `ucs` char(20) DEFAULT '' COMMENT '客户端页面编码',
              `ck` char(1) DEFAULT '' COMMENT '客户端是否支持cookie（1支持，0不支持）',
              `sid` varchar(50) DEFAULT '' COMMENT '客户端唯一编号',
              `uag` varchar(2000) DEFAULT '' COMMENT '用户客端全信息',
              `vs` char(20) DEFAULT '' COMMENT '版本号',
              `uid` int(10) DEFAULT '0' COMMENT '用户编号',
              `sitetype` varchar(255) DEFAULT '' COMMENT '网站类型 tuliu_pc|tuliu_wap',
              PRIMARY KEY (`id`)
                ) ENGINE=MyISAM DEFAULT CHARSET=utf8;
                '''%(self.table_name)
            self.cur.execute(sql_drop)
            self.cur.execute(sql_create)
            self.conn.commit()
        elif self.url_parse_kw['type'] == 'click':
            sql_drop='drop table if exists `%s`'%(self.table_name)
            sql_create='''
                CREATE TABLE `%s` (
              `id` int(20) unsigned NOT NULL AUTO_INCREMENT,
              `time` datetime DEFAULT NULL COMMENT '访问时间',
              `ip` varchar(22) DEFAULT NULL COMMENT 'ip地址',
              `status` int(5) DEFAULT '0' COMMENT '状态码',
              `lgt` char(1) DEFAULT '' COMMENT '页面事件类型（1为页面初始化）',
              `dm` varchar(1000) DEFAULT '' COMMENT '访问域名',
              `rf` varchar(2000) DEFAULT '' COMMENT '上一页来源地址',
              `url` varchar(2000) DEFAULT '' COMMENT '当前访问URL',
              `tt` varchar(1000) DEFAULT '' COMMENT '访问地址的标题',
              `rlt` varchar(500) DEFAULT '' COMMENT '用户屏幕(高度+宽度)',
              `dt` int(10) DEFAULT '0' COMMENT '目标设备或缓冲器上的调色板的比特深度',
              `lu` char(20) DEFAULT '' COMMENT '客户端语言设置',
              `bs` varchar(100) DEFAULT '' COMMENT '浏览器类型',
              `os` varchar(50) DEFAULT '' COMMENT '客户端系统类型',
              `ct` varchar(50) DEFAULT '' COMMENT '客户端访问手机类型',
              `ucs` char(20) DEFAULT '' COMMENT '客户端页面编码',
              `ck` char(1) DEFAULT '' COMMENT '客户端是否支持cookie（1支持，0不支持）',
              `sid` varchar(50) DEFAULT '' COMMENT '客户端唯一编号',
              `uag` varchar(2000) DEFAULT '' COMMENT '用户客端全信息',
              `vs` char(20) DEFAULT '' COMMENT '版本号',
              `uid` int(10) DEFAULT '0' COMMENT '用户编号',
              `sitetype` varchar(255) DEFAULT '' COMMENT '网站类型 tuliu_pc|tuliu_wap',
              `event` varchar(500) DEFAULT '' COMMENT '点击事件名称',
              PRIMARY KEY (`id`)
                ) ENGINE=MyISAM DEFAULT CHARSET=utf8;
                '''%(self.table_name)
            self.cur.execute(sql_drop)
            self.cur.execute(sql_create)
            self.conn.commit()
        else:
            pass

    def parse_log_pv(self):
        '''解析日志访问行为并写入数据库'''
        for log_name in self.log_name_iter():
            f = gzip.open(log_name, 'rb')  # 打开压缩文件对象
            line = f.readline().decode('utf-8')  # 获取第1行数据
            i = 0
            while line:
                i += 1
                print(str(log_name)+'___'+str(i))
                pattern = re.compile(
                    r'(.*) - - \[(.*) \+\d+\] \"(GET|POST) (.*) .*\" (\d+) (\d+) \"(.*?)\" \"(.*?)\".*- (.*) -')
                m = pattern.search(line)
                line = f.readline().decode('utf-8')  # 获取第2行、第3行。。。。。。数据
                if m != None:
                    ip = m.group(1)  # ip地址
                    time = self.logtime_format(m.group(2))  # 访问时间
                    # method = m.group(3) # 请求方法
                    status = str(m.group(5))  # 状态码
                    # refer = m.group(7) # 来源页面
                    # agent = m.group(8) # 头部信息
                    # host = m.group(9) # 域名
                    url_all = urllib.request.unquote(m.group(4))  # 完整url串
                    pattern_url = re.compile(
                        r'/logimg/1.gif\?lgt=(.*)&dm=(.*)&rf=(.*)&url=(.*)&tt=(.*)&rlt=(.*)&dt=(.*)&lu=(.*)&bs=(.*)&os=(.*)'
                        r'&ct=(.*)&ucs=(.*)&ck=(.*)&sid=(.*)&uag=(.*)&vs=(.*)&uid=(.*)&sitetype=(.*)&rnd=(.*)')
                    m_url = pattern_url.search(url_all)
                    if m_url != None:  # 如果匹配到url
                        lgt = m_url.group(1)  # 页面事件类型（1为页面初始化）
                        dm = m_url.group(2)  # 访问域名
                        rf = m_url.group(3)  # 上一页来源地址
                        url = m_url.group(4)  # 当前访问URL
                        tt = m_url.group(5)  # 访问地址的标题
                        rlt = m_url.group(6)  # 用户屏幕(高度+宽度)
                        dt = m_url.group(7)  # 目标设备或缓冲器上的调色板的比特深度
                        lu = m_url.group(8)  # 客户端语言设置
                        bs = m_url.group(9)  # 浏览器类型
                        os = m_url.group(10)  # 客户端系统类型
                        ct = m_url.group(11)  # 客户端访问手机类型
                        ucs = m_url.group(12)  # 客户端页面编码
                        ck = m_url.group(13)  # 客户端是否支持cookie（1支持，0不支持）
                        sid = m_url.group(14)  # 客户端唯一编号
                        uag = m_url.group(15)  # 用户客端全信息
                        vs = m_url.group(16)  # 版本号
                        uid = m_url.group(17)  # 用户id
                        sitetype = m_url.group(18)  # 网站类型 tuliu_pc|tuliu_wap
                        # 'rnd' : m_url.group(19)  #随机值
                        if self.judge_baiduspider((str(uag))) == False:  # 如果不包含百度爬虫
                            if self.judge_event_id(str(url)) == False:  # 如果不包含event_id
                                if self.judge_url_re(str(url)) == True:  # 如果符合url正则表达式
                                    url = self.parse_url_id(url)
                                    sql = 'insert into `%s`(time,ip,status,lgt,dm,rf,url,tt,rlt,dt,lu,bs,os,ct,ucs,ck,sid,uag,vs,uid,sitetype)'%(self.table_name) \
                                          + ' values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                                    self.cur.execute(sql, (
                                    time, ip, status, lgt, dm, rf, url, tt, rlt, dt, lu, bs, os, ct, ucs, ck, sid, uag, vs, uid,sitetype))  # 写入数据
                                    self.conn.commit()
                                    print(url)


    def parse_log_click(self):
        '''解析日志点击行为并写入数据库'''
        for log_name in self.log_name_iter():
            f = gzip.open(log_name, 'rb')  # 打开压缩文件对象
            line = f.readline().decode('utf-8')  # 获取第1行数据
            i = 0
            while line:
                i += 1
                print(str(log_name)+'___'+str(i))
                pattern = re.compile(
                    r'(.*) - - \[(.*) \+\d+\] \"(GET|POST) (.*) .*\" (\d+) (\d+) \"(.*?)\" \"(.*?)\".*- (.*) -')
                m = pattern.search(line)
                line = f.readline().decode('utf-8')  # 获取第2行、第3行。。。。。。数据
                if m != None:
                    ip = m.group(1)  # ip地址
                    time = self.logtime_format(m.group(2))  # 访问时间
                    # method = m.group(3) # 请求方法
                    status = str(m.group(5))  # 状态码
                    # refer = m.group(7) # 来源页面
                    # agent = m.group(8) # 头部信息
                    # host = m.group(9) # 域名
                    url_all = urllib.request.unquote(m.group(4))  # 完整url串
                    pattern_url = re.compile(
                        r'/logimg/1.gif\?lgt=(.*)&dm=(.*)&rf=(.*)&url=(.*)&tt=(.*)&rlt=(.*)&dt=(.*)&lu=(.*)&bs=(.*)&os=(.*)'
                        r'&ct=(.*)&ucs=(.*)&ck=(.*)&sid=(.*)&uag=(.*)&vs=(.*)&uid=(.*)&sitetype=(.*)&rnd=(.*)&event_id=(.*)')
                    m_url = pattern_url.search(url_all)
                    if m_url != None:  # 如果匹配到url
                        lgt = m_url.group(1)  # 页面事件类型（1为页面初始化）
                        dm = m_url.group(2)  # 访问域名
                        rf = m_url.group(3)  # 上一页来源地址
                        url = m_url.group(4)  # 当前访问URL
                        tt = m_url.group(5)  # 访问地址的标题
                        rlt = m_url.group(6)  # 用户屏幕(高度+宽度)
                        dt = m_url.group(7)  # 目标设备或缓冲器上的调色板的比特深度
                        lu = m_url.group(8)  # 客户端语言设置
                        bs = m_url.group(9)  # 浏览器类型
                        os = m_url.group(10)  # 客户端系统类型
                        ct = m_url.group(11)  # 客户端访问手机类型
                        ucs = m_url.group(12)  # 客户端页面编码
                        ck = m_url.group(13)  # 客户端是否支持cookie（1支持，0不支持）
                        sid = m_url.group(14)  # 客户端唯一编号
                        uag = m_url.group(15)  # 用户客端全信息
                        vs = m_url.group(16)  # 版本号
                        uid = m_url.group(17)  # 用户id
                        sitetype = m_url.group(18)  # 网站类型 tuliu_pc|tuliu_wap
                        # 'rnd' : m_url.group(19)  #随机值
                        event = m_url.group(20)  #点击事件名称
                        if self.judge_event_re(str(event)) == True:  # 如果符合点击事件的正则表达式
                            sql = 'insert into `%s`(time,ip,status,lgt,dm,rf,url,tt,rlt,dt,lu,bs,os,ct,ucs,ck,sid,uag,vs,uid,sitetype,event)'%(self.table_name) \
                                  + ' values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                            self.cur.execute(sql, (
                            time, ip, status, lgt, dm, rf, url, tt, rlt, dt, lu, bs, os, ct, ucs, ck, sid, uag, vs, uid, sitetype, event))  # 写入数据
                            self.conn.commit()
                            print(event)


    def parse_log_type(self):
        '''判断解析类别（区分解析流量事件及点击事件）'''
        if self.url_parse_kw['type'] == 'pv':
            self.parse_log_pv()
        elif self.url_parse_kw['type'] == 'click':
            self.parse_log_click()
        else:
            pass


if __name__ == '__main__':
    test = parse_nglog('2019-04-26','2019-04-26','test7_table','/s-view-(\d+)',type = 'pv',parse_id = False)
    test.create_table() #建表
    test.parse_log_type() #解析日志
    test.close_dbconn() #断开数据库连接
