###nginx日志入库（log.gz压缩文件）

import gzip
import re
import pymysql

f = gzip.open("F:/rizhi/access_20190128.napp1.log.gz", 'rb')#打开压缩文件对象

conn = pymysql.connect(
        host="******",
        user="******",
        password="*****",
        port=3306,
        charset="utf8",
        db="test")
cur = conn.cursor()

try:
    line=f.readline().decode('utf-8')#获取第1行数据
    while line:
        pattern = re.compile(r'(.*) - - \[(.*) \+\d+\] \"(GET|POST) (.*) .*\" (\d+) (\d+) \"(.*?)\" \"(.*?)\".*- (.*) -')#匹配所需数据
        m = pattern.search(line)
        line=f.readline().decode('utf-8')#获取第2行、第3行。。。。。。数据
        if m != None:#如果匹配成功
            ip=m.group(1)#获取ip
            time=m.group(2)#获取时间
            method=m.group(3)#获取request方法
            url=m.group(4)#获取url
            status=str(m.group(5))#获取状态码
            refer=m.group(7)#获取来源页面
            agent=m.group(8)#获取头部信息
            host=m.group(9)#获取域名

            
            sql='insert into nginx_log(ip,time,method,url,status,refer,agent,host) values(%s,%s,%s,%s,%s,%s,%s,%s)'
            cur.execute(sql,(ip,time,method,url,status,refer,agent,host))#执行插入数据
            conn.commit()
        
finally:
    f.close() #关闭文件流
    cur.close()#关闭游标
    conn.close()

	
	
	
	
	
	
###nginx日志入库（未压缩格式）

import re
import pymysql

f = open('F:/rizhi/access_20190128.napp2.log','r')#打开文件对象

conn = pymysql.connect(
        host="*****",
        user="*****",
        password="*****",
        port=3306,
        charset="utf8",
        db="test")
cur = conn.cursor()

try:
    for line in f:
        pattern = re.compile(r'(.*) - - \[(.*) \+\d+\] \"(GET|POST) (.*) .*\" (\d+) (\d+) \"(.*?)\" \"(.*?)\".*- (.*) -')#匹配所需数据
        m = pattern.search(line)
        if m != None:#如果匹配成功
            ip=m.group(1)#获取ip
            time=m.group(2)#获取时间
            method=m.group(3)#获取request方法
            url=m.group(4)#获取url
            status=str(m.group(5))#获取状态码
            refer=m.group(7)#获取来源页面
            agent=m.group(8)#获取头部信息
            host=m.group(9)#获取域名

            
            sql='insert into nginx_log(ip,time,method,url,status,refer,agent,host) values(%s,%s,%s,%s,%s,%s,%s,%s)'
            cur.execute(sql,(ip,time,method,url,status,refer,agent,host))#执行插入数据
            conn.commit()
        
finally:
    f.close() #关闭文件流
    cur.close()#关闭游标
    conn.close()







###nginx pc/wap端详细日志入库（log.gz压缩文件）

import gzip
import re
import numpy as np
import urllib.request
import pymysql
import time

add_date=time.strftime("%Y-%m-%d") #获取今天日期

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
    file_name="F:/nginx_log/trace-web.tuliu.com/access_"+ log_date + ".log.gz" #日志文件名
    f = gzip.open(file_name, 'rb')#打开压缩文件对象

    conn = pymysql.connect(
            host="*****",
            user="*****",
            password="*****",
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
                ip = m.group(1) #ip
                time = logtime_format(m.group(2)) #访问时间
                #method = m.group(3) #请求方法
                status = str(m.group(5)) #状态码
                refer = m.group(7) #来源页面
                agent = m.group(8) #头部信息
                host = m.group(9) #域名

                url_all = urllib.request.unquote(m.group(4)) #完整url窜
                pattern_url = re.compile(
                    r'/logimg/1.gif\?lgt=(.*)&dm=(.*)&rf=(.*)&url=(.*)&tt=(.*)&rlt=(.*)&dt=(.*)&lu=(.*)&bs=(.*)&os=(.*)'
                    r'&ct=(.*)&ucs=(.*)&ck=(.*)&sid=(.*)&uag=(.*)&vs=(.*)&uid=(.*)&sitetype=(.*)&rnd=(.*)')
                m_url = pattern_url.search(url_all)
                if m_url != None: #E如果匹配到url
                    url_g = m_url.group(0) #完整url窜
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

                    sql='insert into nglog_pc_wap(time,status,lgt,dm,rf,url,tt,rlt,dt,lu,bs,os,ct,ucs,ck,sid,uag,vs,uid,sitetype,add_date)' \
                        ' values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                    cur.execute(sql,(time,status,lgt,dm,rf,url,tt,rlt,dt,lu,bs,os,ct,ucs,ck,sid,uag,vs,uid,sitetype,add_date))#执行插入数据
                    conn.commit()
                    print('已插入第'+str(i)+'条记录')
    finally:
        f.close() #关闭文件流
        cur.close()#关闭游标
        print(file_name+'  数据写入完毕')

if __name__ == '__main__':
    log_write('20190224')









###nginx pc/wap端详细日志入库（log.gz压缩文件）
import gzip
import re
import numpy as np
import urllib.request
import pymysql
import time

add_date=time.strftime("%Y-%m-%d") #获取今天日期,用户写入数据库时的提交时间

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
    file_name="/mnt/log/trace-android-app.tuliu.com/access_"+ log_date + ".log.gz" #日志文件名
    f = gzip.open(file_name, 'rb')#打开压缩文件对象

    conn = pymysql.connect(
            host="******",
            user="******",
            password="******",
            port=3306,
            charset="utf8",
            db="nginx_log")
    cur = conn.cursor()


    line=f.readline().decode('utf-8')#获取第1行数据
    i = 0
    while line:
        i += 1  # 计数
        pattern = re.compile(r'(.*) - - \[(.*) \+\d+\] \"(GET|POST) (.*) .*\" (\d+) (\d+) \"(.*?)\" \"(.*?)\".*- (.*) -')
        m = pattern.search(line)
        line = f.readline().decode('utf-8')  # 获取第2行、第3行。。。。。。数据
        if m != None:
            ip = m.group(1) #ip地址
            time = logtime_format(m.group(2)) #访问时间
            #method = m.group(3) #请求方法
            status = str(m.group(5)) #状态码
            refer = m.group(7) #来源页面
            agent = m.group(8) #头部信息
            #host = m.group(9) #域名

            url_all = urllib.request.unquote(m.group(4)) #完整url串
            pattern_url = re.compile(r'/\?(.*)&&(.*)&&(.*)&&(.*)&&(.*)&&(.*)&&(.*)&&(.*)&&(.*)&&(.*)&&(.*)&&(.*)&&(.*)')
            m_url = pattern_url.search(url_all)
            if m_url != None: #E如果匹配到url
                #url_g = m_url.group(0) #完整url串
                uid = m_url.group(1) #用户id
                dk = m_url.group(2) #端口名
                vsc = m_url.group(3) #版本code
                vsn = m_url.group(4) #版本name
                pp = m_url.group(5) #手机品牌
                xt = m_url.group(6) #手机系统版本
                ipd = m_url.group(7) #ip地址
                imei = m_url.group(8) #IMEI码
                jd = m_url.group(9) #经度
                wd = m_url.group(10) #维度
                #tm = m_url.group(11) #时间
                xw = m_url.group(12) #操作行为名称
                qt = m_url.group(13) #土地详情页为（土地id-1为服务中心 2为主站） 资讯详情页为url 搜索为搜索词等等

                sql='insert into nglog_app(time,ip,status,refer,agent,uid,dk,vsc,vsn,pp,xt,ipd,imei,jd,wd,xw,qt,add_date)' \
                    ' values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                cur.execute(sql,(time,ip,status,refer,agent,uid,dk,vsc,vsn,pp,xt,ipd,imei,jd,wd,xw,qt,add_date))#执行插入数据
                conn.commit()
                print('已插入第'+str(i)+'条记录')



if __name__ == '__main__':

    #logdate=time.strftime("%Y%m%d") #今天的log文件写入数据库
    log_write('20190301')
