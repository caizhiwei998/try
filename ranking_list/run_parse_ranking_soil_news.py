import datetime
import pymysql
from parse_ranking_soil_news import  parse_nglog_web,parse_nglog_app

dbconn = pymysql.connect(
    host="10.10.66.8",
    user="caizhiwei",
    password="20180803",
    db="ranking_list",
    port=3306,
    charset='utf8'
    )
cur = dbconn.cursor()
sql_select_max_date = 'SELECT max(log_date) from ranking_soil_news_daily'
cur.execute(sql_select_max_date)
max_date = cur.fetchall()[0][0] #数据库获取排行表中最大的日期做为起始日期
cur.close()
dbconn.close()

datestart= str(max_date)
dateend = str((datetime.date.today() + datetime.timedelta(days=-1)).strftime("%Y-%m-%d"))

starttime_web = datetime.datetime.now() #记录web日志解析起始时间
parse_web = parse_nglog_web(datestart, dateend) #实例化web日志解析类
parse_web.parse_log_pv() #分析日志
parse_web.data_delete() #删除90天以上数据
parse_web.close_dbconn() #关闭数据库
endtime_web = datetime.datetime.now() #记录web日志解析结束时间
costtime_web = endtime_web - starttime_web #计算解析运行时间
print('解析web日志程序运行时间： ' + str(costtime_web))

starttime_app = datetime.datetime.now() #记录app日志解析起始时间
parse_app = parse_nglog_app(datestart, dateend) #实例化app日志解析类
parse_app.parse_log_pv() #分析日志
parse_app.close_dbconn() #关闭数据库
endtime_app = datetime.datetime.now() #记录app日志解析结束时间
costtime_app = endtime_app - starttime_app #计算解析运行时间
print('解析app日志程序运行时间： ' + str(costtime_app))


