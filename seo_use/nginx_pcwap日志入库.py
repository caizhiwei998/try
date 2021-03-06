import gzip
import re
import numpy as np
import urllib.request
import pymysql
import time
import arrow


add_date=time.strftime("%Y-%m-%d") #获取今天日期,用于写入数据库时的提交时间

#nginx日志日期转化为便于数据库存储的格式
def logtime_format(logtime):
    en_mon=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    num_mon=['01','02','03','04','05','06','07','08','09','10','11','12']

    pattern_time = re.compile(r'(\d+)/(\w+)/(\d+):(\d+):(\d+):(\d+)')
    m_time = pattern_time.search(logtime)
    year=m_time.group(3)
    mon=m_time.group(2)
    for i in np.arange(12):
        if mon == en_mon[i]:
            mon = num_mon[i]
    day=m_time.group(1)
    h=m_time.group(4)
    m=m_time.group(5)
    s=m_time.group(6)
    return(year+'-'+mon+'-'+day+' '+h+':'+m+':'+s+'')

#日志写入数据库
def log_write(log_date): #传入log日期，如‘20190224’
    file_name="/mnt/log/trace-web.tuliu.com/access_"+ log_date + ".log.gz" #日志文件名
    f = gzip.open(file_name, 'rb')#打开压缩文件对象

    conn = pymysql.connect(
            host="******",
            user="******",
            password="******",
            port=3306,
            charset="utf8",
            db="nginx_log")
    cur = conn.cursor()

    try:
        line=f.readline().decode('utf-8')#获取第1行数据
        i=0
        while line:
            i+=1 #计数
            pattern = re.compile(r'(.*) - - \[(.*) \+\d+\] \"(GET|POST) (.*) .*\" (\d+) (\d+) \"(.*?)\" \"(.*?)\".*- (.*) -')#匹配所需数据
            m = pattern.search(line)
            line=f.readline().decode('utf-8')#获取第2行、第3行。。。。。。数据
            if m != None:
                ip = m.group(1) #ip地址
                time = logtime_format(m.group(2)) #访问时间
                #method = m.group(3) #请求方法
                status = str(m.group(5)) #状态码
                #refer = m.group(7) #来源页面
                #agent = m.group(8) #头部信息
                #host = m.group(9) #域名

                url_all = urllib.request.unquote(m.group(4)) #完整url串
                pattern_url = re.compile(
                    r'/logimg/1.gif\?lgt=(.*)&dm=(.*)&rf=(.*)&url=(.*)&tt=(.*)&rlt=(.*)&dt=(.*)&lu=(.*)&bs=(.*)&os=(.*)'
                    r'&ct=(.*)&ucs=(.*)&ck=(.*)&sid=(.*)&uag=(.*)&vs=(.*)&uid=(.*)&sitetype=(.*)&rnd=(.*)')
                m_url = pattern_url.search(url_all)
                if m_url != None: #E如果匹配到url
                    #url_g = m_url.group(0) #完整url串
                    lgt = m_url.group(1) #页面事件类型（1为页面初始化）
                    dm = m_url.group(2) #访问域名
                    rf = m_url.group(3) #上一页来源地址
                    url = m_url.group(4) #当前访问URL
                    tt = m_url.group(5) #访问地址的标题
                    rlt = m_url.group(6) #用户屏幕(高度+宽度)
                    dt = m_url.group(7) #目标设备或缓冲器上的调色板的比特深度
                    lu = m_url.group(8) #客户端语言设置
                    bs = m_url.group(9) #浏览器类型
                    os = m_url.group(10) #客户端系统类型
                    ct = m_url.group(11) #客户端访问手机类型
                    ucs = m_url.group(12) #客户端页面编码
                    ck = m_url.group(13) #客户端是否支持cookie（1支持，0不支持）
                    sid = m_url.group(14) #客户端唯一编号
                    uag = m_url.group(15) #用户客端全信息
                    vs = m_url.group(16) #版本号
                    uid = m_url.group(17) #用户id
                    sitetype = m_url.group(18) #网站类型 tuliu_pc|tuliu_wap
                    #rnd = m_url.group(19) #随机值

                    sql='insert into nglog_pcwap(time,ip,status,lgt,dm,rf,url,tt,rlt,dt,lu,bs,os,ct,ucs,ck,sid,uag,vs,uid,sitetype,add_date)' \
                        ' values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                    cur.execute(sql,(time,ip,status,lgt,dm,rf,url,tt,rlt,dt,lu,bs,os,ct,ucs,ck,sid,uag,vs,uid,sitetype,add_date))#执行插入数据
                    conn.commit()
                    #print('已插入第'+str(i)+'条记录')

    finally:
        f.close() #关闭文件流
        cur.close()#关闭游标
        conn.close()
        print(file_name + '  数据写入完毕')
        print('共写入' + str(i) + '条数据')

def rename_table(last_mon):
    conn = pymysql.connect(
            host="******",
            user="******",
            password="******",
            port=3306,
            charset="utf8",
            db="nginx_log")
    cur = conn.cursor()
    #表按月存储
    backup_table_name="nglog_pcwap_"+last_mon
    sql_rename_table='rename table nglog_pcwap to `%s`'%(backup_table_name)
    sql_create_backup_table='create table nglog_pcwap like `%s`'%(backup_table_name)
    cur.execute(sql_rename_table)
    cur.execute(sql_create_backup_table)
    cur.close()
    conn.close()


def delete_insert(): #上月表中本月初数据移至本月表
    last_mon = arrow.now().shift(months=-1).format("YYYYMM")
    this_mon_01 = arrow.now().format("YYYY-MM-01")
    backup_table_name = "nglog_pcwap_" + last_mon
    conn = pymysql.connect(
            host="******",
            user="******",
            password="******",
            port=3306,
            charset="utf8",
            db="nginx_log")
    cur = conn.cursor()
    sql_insert_last="insert into nglog_pcwap select * from `%s` where time >='%s' "%(backup_table_name,this_mon_01)
    sql_delete_last="delete from `%s` where time >='%s' "%(backup_table_name,this_mon_01)
    cur.execute(sql_insert_last)
    cur.execute(sql_delete_last)
    cur.close()
    conn.close()

if __name__ == '__main__':
    print('-'*60)
    if time.strftime("%Y%m%d")[-2:]=='02':#每月2号备份表
        last_mon = arrow.now().shift(months=-1).format("YYYYMM")
        rename_table(last_mon)
        print('表已rename')

    print('开始解析pc/wap日志')
    logdate=time.strftime("%Y%m%d") #今天的log文件写入数据库
    log_write(logdate)

    if time.strftime("%Y%m%d")[-2:]=='02':#每月2号调整上月底数据
        delete_insert()
        print('上月底数据调整完毕')

