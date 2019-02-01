import gzip
import re
import pymysql
import datetime
import numpy as np


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

#获取今天之前n天日期列表
def get_nday_list(n):
    before_n_days = []
    for i in range(1, n + 1)[::-1]:
        before_n_days.append(str((datetime.date.today() - datetime.timedelta(days=i)).strftime('%Y%m%d')))
    return before_n_days

log_date_list = get_nday_list(31)
last_log_name=[".napp1.log.gz",".napp2.log.gz"]

for day in log_date_list:
    for l_name in last_log_name:
        f = gzip.open("/mnt/log/www.tuliu.com/access_"+day+l_name, 'rb')  # 打开压缩文件对象

        conn = pymysql.connect(
            host="10.10.66.8",
            user="caizhiwei",
            password="*****",
            port=3306,
            charset="utf8",
            db="seo_cai")
        cur = conn.cursor()

        try:
            line = f.readline().decode('utf-8')  # 获取第1行数据
            while line:
                pattern = re.compile(
                    r'(.*) - - \[(.*) \+\d+\] \"(GET|POST) (.*) .*\" (\d+) (\d+) \"(.*?)\" \"(.*?)\".*- (.*) -')  # 匹配每条日志数据
                m = pattern.search(line)
                line = f.readline().decode('utf-8')  # 获取第2行、第3行。。。。。。数据
                if m != None and m.group(5)=='200':  # 如果匹配成功 且状态码为200
                    #ip = m.group(1)  # 获取ip
                    time = logtime_format(m.group(2))  # 获取时间
                    #method = m.group(3)  # 获取request方法
                    url = m.group(4)  # 获取url
                    #status = str(m.group(5))  # 获取状态码
                    #refer = m.group(7)  # 获取来源页面
                    #agent = m.group(8)  # 获取头部信息
                    #host = m.group(9)  # 获取域名
                    pattern_url = re.compile(r'.*?(s-view|view)-(\d+).*')  #匹配土地详情页
                    m_url = pattern_url.search(url)
                    if m_url != None:
                        src=m_url.group(1) #土地来源
                        sid=m_url.group(2) #土地id
                        add_date = datetime.date.today().strftime('%Y%m%d') #添加日期
                        cursor = conn.cursor()
                        sql = 'insert into nglog_spv(time,src,sid,add_date) values(%s,%s,%s,%s)'
                        cur.execute(sql, (time,src,sid,add_date))  # 执行插入数据
                        conn.commit()
                        print(time+'_'+src+'_'+sid+'_'+add_date)

        finally:
            f.close()  # 关闭文件流
            cur.close()  # 关闭游标
