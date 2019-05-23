import datetime
from get_soil_news_rank import soil_news_rank

starttime = datetime.datetime.now()
get_rank = soil_news_rank()
rank_soil = get_rank.get_soil_rank() #运行土地30天排行数据
rank_news = get_rank.get_news_rank() #运行资讯7天排行数据
get_rank.close_dbconn()
endtime = datetime.datetime.now()
costtime = endtime - starttime
print('处理土地及资讯排行用时： ' + str(costtime))