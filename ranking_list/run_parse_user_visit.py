import datetime
import pymysql
from parse_user_visit import  parse_user_visit_web,parse_user_visit_app


dbconn = pymysql.connect(
    host="******",
    user="******",
    password="******",
    db="ranking_list",
    port=3306,
    charset='utf8'
    )
cur = dbconn.cursor()
sql_select_max_date = 'SELECT max(log_date) from ranking_user_visit_score'
cur.execute(sql_select_max_date)
max_date = cur.fetchall()[0][0] #数据库获取表中最大的日期做为起始日期
cur.close()
dbconn.close()

datestart= str(max_date)
dateend = str((datetime.date.today() + datetime.timedelta(days=-1)).strftime("%Y-%m-%d"))


starttime_web = datetime.datetime.now() #记录起始时间
visit_web = parse_user_visit_web(datestart,dateend)
visit_web.parse_log_pv()
visit_web.data_delete()
visit_web.close_dbconn()
endtime_web = datetime.datetime.now() #记录结束时间
costtime_web = endtime_web - starttime_web #计算解析运行时间
print('解析用户访问web程序运行时间： ' + str(costtime_web))


starttime_app = datetime.datetime.now() #记录app日志解析起始时间
visit_app = parse_user_visit_web(datestart,dateend)
visit_app.parse_log_pv()
visit_app.data_delete()
visit_app.close_dbconn()
endtime_app = datetime.datetime.now() #记录app日志解析结束时间
costtime_app = endtime_app - starttime_app #计算解析运行时间
print('解析用户访问app程序运行时间： ' + str(costtime_app))
