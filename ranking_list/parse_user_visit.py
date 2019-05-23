import datetime
import pymysql
import re
import numpy as np
import gzip
import urllib.request


class parse_user_visit_web:
    '''解析web端用户访问土地及资讯'''
    def __init__(self,datestart,dateend):
        self.datestart = datestart
        self.dateend = dateend
        self.today = datetime.date.today().strftime("%Y-%m-%d")
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
        date = str(year) + '-' + str(mon) + '-' + str(day)
        return date


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


    def dbconn_nglog_analyse(self):
        '''排行榜数据库连接'''
        dbconn = pymysql.connect(
            host="10.10.66.8",
            user="caizhiwei",
            password="20180803",
            db="ranking_list",
            port=3306,
            charset='utf8'
        )
        return dbconn


    def close_dbconn(self):
        '''关闭数据库连接、游标'''
        self.conn.close()
        self.cur.close()


    def judge_user_visit_type(self,url):
        '''判断用户访问土地还是资讯，土地返回2，资讯返回1'''
        pattern_soil_sv = re.compile(r'/s-view-(\d+)') #匹配服务中心土地
        m_soil_sv = pattern_soil_sv.search(url)
        pattern_soil_tl = re.compile(r'/view-(\d+)') #匹配主站土地
        m_soil_tl = pattern_soil_tl.search(url)
        pattern_news_wap = re.compile(r'm.tuliu.com/.*?wnews/read-(\d+).html') #匹配wap端资讯
        m_news_wap = pattern_news_wap.search(url)
        pattern_news_pc = re.compile(r'tuliu.com/read-(\d+).html') #匹配pc端资讯
        m_news_pc = pattern_news_pc.search(url)
        if m_soil_sv != None:
            score = 2
        elif m_soil_tl != None:
            score = 2
        elif m_news_wap != None:
            score = 1
        elif m_news_pc != None:
            score = 1
        else:
            score = 0
        return score


    def data_update(self,log_date,uid,score):
        '''数据库数据更新'''
        if uid.isdigit() is True and int(uid) > 0 and score >0:
            sql_find_id = 'select uid from ranking_user_visit_score where log_date = "%s" and uid = %s'%(log_date,uid)
            self.cur.execute(sql_find_id)
            find_id = self.cur.fetchall()
            if len(find_id)>0:
                sql_update='update ranking_user_visit_score set score=score+%s where log_date = "%s" and uid = %s'%(score,log_date,uid)
                self.cur.execute(sql_update)
                self.conn.commit()
                #print(sql_update)
            else:
                sql_insert="insert into ranking_user_visit_score(log_date,add_date,uid,score) values(%s,%s,%s,%s)"
                self.cur.execute(sql_insert,(log_date,self.today,uid,score))
                self.conn.commit()
                #print(sql_insert)


    def data_delete(self):
        sql_delete = 'delete from ranking_user_visit_score where log_date < DATE_SUB(CURDATE(), INTERVAL 90 day)'
        self.cur.execute(sql_delete)
        self.conn.commit()


    def parse_log_pv(self):
        '''解析日志访问行为并写入数据库'''
        for log_name in self.log_name_iter():
            f = gzip.open(log_name, 'rb')  # 打开压缩文件对象
            line = f.readline().decode('utf-8')  # 获取第1行数据
            #i = 0
            while line:
                #i += 1
                #print(str(log_name)+'___'+str(i))
                pattern = re.compile(
                    r'(.*) - - \[(.*) \+\d+\] \"(GET|POST) (.*) .*\" (\d+) (\d+) \"(.*?)\" \"(.*?)\".*- (.*) -')
                m = pattern.search(line)
                line = f.readline().decode('utf-8')  # 获取第2行、第3行。。。。。。数据
                if m != None:
                    #ip = m.group(1)  # ip地址
                    date = self.logtime_format(m.group(2))  # 访问时间
                    # method = m.group(3) # 请求方法
                    #status = str(m.group(5))  # 状态码
                    # refer = m.group(7) # 来源页面
                    # agent = m.group(8) # 头部信息
                    # host = m.group(9) # 域名
                    url_all = urllib.request.unquote(m.group(4))  # 完整url串
                    pattern_url = re.compile(
                        r'/logimg/1.gif\?lgt=(.*)&dm=(.*)&rf=(.*)&url=(.*)&tt=(.*)&rlt=(.*)&dt=(.*)&lu=(.*)&bs=(.*)&os=(.*)'
                        r'&ct=(.*)&ucs=(.*)&ck=(.*)&sid=(.*)&uag=(.*)&vs=(.*)&uid=(.*)&sitetype=(.*)&rnd=(.*)')
                    m_url = pattern_url.search(url_all)
                    if m_url != None:  # 如果匹配到url
                        #lgt = m_url.group(1)  # 页面事件类型（1为页面初始化）
                        #dm = m_url.group(2)  # 访问域名
                        #rf = m_url.group(3)  # 上一页来源地址
                        url = m_url.group(4)  # 当前访问URL
                        #tt = m_url.group(5)  # 访问地址的标题
                        #rlt = m_url.group(6)  # 用户屏幕(高度+宽度)
                        #dt = m_url.group(7)  # 目标设备或缓冲器上的调色板的比特深度
                        #lu = m_url.group(8)  # 客户端语言设置
                        #bs = m_url.group(9)  # 浏览器类型
                        #os = m_url.group(10)  # 客户端系统类型
                        #ct = m_url.group(11)  # 客户端访问手机类型
                        #ucs = m_url.group(12)  # 客户端页面编码
                        #ck = m_url.group(13)  # 客户端是否支持cookie（1支持，0不支持）
                        #sid = m_url.group(14)  # 客户端唯一编号
                        uag = m_url.group(15)  # 用户客端全信息
                        #vs = m_url.group(16)  # 版本号
                        uid = m_url.group(17)  # 用户id
                        #sitetype = m_url.group(18)  # 网站类型 tuliu_pc|tuliu_wap
                        # 'rnd' : m_url.group(19)  #随机值
                        if self.judge_baiduspider((str(uag))) == False:  # 如果不包含百度爬虫
                            if self.judge_event_id(str(url)) == False:  # 如果不包含event_id
                                score = self.judge_user_visit_type(url)
                                self.data_update(date, uid, score)


class parse_user_visit_app(parse_user_visit_web):
    '''解析app端用户访问土地及资讯，继承parse_user_visit_web，并覆写3个函数'''
    def __init__(self,datestart,dateend):
        parse_user_visit_web.__init__(self,datestart,dateend)


    def log_name_iter(self):
        '''需要读取数据的日志文件名迭代器'''
        for log_date in self.log_date_list:
            log_name = "/mnt/log/trace-android-app.tuliu.com/access_" + log_date + ".log.gz"
            yield log_name


    def data_update(self,log_date,uid,xw):
        '''数据库数据更新'''
        if uid.isdigit() is True and int(uid) > 0 :
            if xw == '浏览-土地供应详情':
                sql_find_id = 'select uid from ranking_user_visit_score where log_date = "%s" and uid = %s'%(log_date,uid)
                self.cur.execute(sql_find_id)
                find_id = self.cur.fetchall()
                if len(find_id)>0:
                    sql_update='update ranking_user_visit_score set score=score+2 where log_date = "%s" and uid = %s'%(log_date,uid)
                    self.cur.execute(sql_update)
                    self.conn.commit()
                    #print(sql_update)
                else:
                    sql_insert="insert into ranking_user_visit_score(log_date,add_date,uid,score) values(%s,%s,%s,'2')"
                    self.cur.execute(sql_insert,(log_date,self.today,uid))
                    self.conn.commit()
                    #print(sql_insert)
            elif xw == '浏览-资讯详情':
                sql_find_id = 'select uid from ranking_user_visit_score where log_date = "%s" and uid = %s'%(log_date,uid)
                self.cur.execute(sql_find_id)
                find_id = self.cur.fetchall()
                if len(find_id)>0:
                    sql_update='update ranking_user_visit_score set score=score+1 where log_date = "%s" and uid = %s'%(log_date,uid)
                    self.cur.execute(sql_update)
                    self.conn.commit()
                    #print(sql_update)
                else:
                    sql_insert="insert into ranking_user_visit_score(log_date,add_date,uid,score) values(%s,%s,%s,'1')"
                    self.cur.execute(sql_insert,(log_date,self.today,uid))
                    self.conn.commit()
                    #print(sql_insert)
            else:
                pass


    def parse_log_pv(self):
        '''解析日志访问行为并写入数据库'''
        for log_name in self.log_name_iter():
            f = gzip.open(log_name, 'rb')  # 打开压缩文件对象
            line = f.readline().decode('utf-8')  # 获取第1行数据
            #i = 0
            while line:
                #i += 1
                #print(str(log_name)+'___'+str(i))
                pattern = re.compile(
                    r'(.*) - - \[(.*) \+\d+\] \"(GET|POST) (.*) .*\" (\d+) (\d+) \"(.*?)\" \"(.*?)\".*- (.*) -')
                m = pattern.search(line)
                line = f.readline().decode('utf-8')  # 获取第2行、第3行。。。。。。数据
                if m != None:
                    #ip = m.group(1)  # ip地址
                    date = self.logtime_format(m.group(2))  # 访问时间
                    # method = m.group(3) # 请求方法
                    #status = str(m.group(5))  # 状态码
                    # refer = m.group(7) # 来源页面
                    # agent = m.group(8) # 头部信息
                    # host = m.group(9) # 域名
                    url_all = urllib.request.unquote(m.group(4))  # 完整url串
                    pattern_url = re.compile(
                        r'/\?(.*)&&(.*)&&(.*)&&(.*)&&(.*)&&(.*)&&(.*)&&(.*)&&(.*)&&(.*)&&(.*)&&(.*)&&(.*)')
                    m_url = pattern_url.search(url_all)
                    if m_url != None:  # 如果匹配到url
                        uid = m_url.group(1)  # 用户id
                        # dk = m_url.group(2)  # 端口名
                        # vsc = m_url.group(3)  # 版本code
                        # vsn = m_url.group(4)  # 版本name
                        # pp = m_url.group(5)  # 手机品牌
                        # xt = m_url.group(6)  # 手机系统版本
                        # ipd = m_url.group(7)  # ip地址
                        # imei = m_url.group(8)  # IMEI码
                        # jd = m_url.group(9)  # 经度
                        # wd = m_url.group(10)  # 维度
                        # # tm = m_url.group(11) #时间
                        xw = m_url.group(12)  # 操作行为名称
                        # qt = m_url.group(13)  # 土地详情页为（土地id-1为服务中心 2为主站） 资讯详情页为url
                        self.data_update(date, uid, xw)







