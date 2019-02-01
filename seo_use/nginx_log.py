#nginx日志入库（log.gz压缩文件）

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

            cursor = conn.cursor()
            sql='insert into nginx_log(ip,time,method,url,status,refer,agent,host) values(%s,%s,%s,%s,%s,%s,%s,%s)'
            cur.execute(sql,(ip,time,method,url,status,refer,agent,host))#执行插入数据
            conn.commit()
        
finally:
    f.close() #关闭文件流
    cur.close()#关闭游标

	
	
	
	
	
	
#nginx日志入库（未压缩格式）

import re
import pymysql

f = open('F:/rizhi/access_20190128.napp2.log','r')#打开文件对象

conn = pymysql.connect(
        host="10.10.66.8",
        user="caizhiwei",
        password="20180803",
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

            cursor = conn.cursor()
            sql='insert into nginx_log(ip,time,method,url,status,refer,agent,host) values(%s,%s,%s,%s,%s,%s,%s,%s)'
            cur.execute(sql,(ip,time,method,url,status,refer,agent,host))#执行插入数据
            conn.commit()
        
finally:
    f.close() #关闭文件流
    cur.close()#关闭游标
