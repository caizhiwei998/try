import datetime
from get_user_rank import user_rank


starttime = datetime.datetime.now() #记录起始时间
datestart = str((datetime.date.today() + datetime.timedelta(days=-7)).strftime("%Y-%m-%d"))
dateend = str((datetime.date.today() + datetime.timedelta(days=-1)).strftime("%Y-%m-%d"))
user_score = user_rank(datestart, dateend)
user_score.data_insert()
user_score.close_dbconn_tuliu_v2()
user_score.close_dbconn_ranking_list()
endtime = datetime.datetime.now() #记录结束时间
costtime = endtime - starttime #计算解析运行时间
print('计算用户得分运行时间： ' + str(costtime))