import datetime
import pymysql

class soil_news_rank:
    def __init__(self):
        self.conn = self.dbconn()
        self.cur = self.conn.cursor()


    def dbconn(self):
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
        self.cur.close()
        self.conn.close()


    def get_date_start_end(self,days_ago1,days_ago2):
        '''days_ago1，days_ago1都为N天前，days_ago1>=days_ago2，获得起始日期'''
        datestart = (datetime.date.today() + datetime.timedelta(days=-days_ago1)).strftime("%Y-%m-%d")
        dateend = (datetime.date.today() + datetime.timedelta(days=-days_ago2)).strftime("%Y-%m-%d")
        date_start_end = [datestart,dateend]
        return date_start_end


    def get_soil_rank(self):
        '''获取近30天土地详情页流量排名并更新至数据库'''
        datestart = self.get_date_start_end(30,1)[0]
        dateend = self.get_date_start_end(30,1)[1]
        sql_select = '''
        SELECT url_id,src,sum(pv) from ranking_soil_news_daily 
        where src in (1,2) and url_id != 0 and log_date BETWEEN '%s' and '%s'
        group by url_id,src order by sum(pv) desc
        '''%(datestart,dateend)
        self.cur.execute(sql_select)
        data_soil_rank = self.cur.fetchall()
        sql_delete='delete from ranking_soil_30days where update_date < DATE_SUB(CURDATE(), INTERVAL 3 day)' #清除3天前数据
        self.cur.execute(sql_delete)
        for row in data_soil_rank:
            soil_id = row[0]
            src = row[1]
            soil_pv = row[2]
            today = datetime.date.today().strftime("%Y-%m-%d")
            sql_update = 'insert into ranking_soil_30days(update_date,soil_id,pv,src) values(%s,%s,%s,%s)'
            self.cur.execute(sql_update,(today,soil_id,soil_pv,src))
            self.conn.commit()
            #print([today,soil_id,soil_pv,src])
        print(sql_select)


    def get_news_rank(self):
        '''获取近7天资讯详情页流量排名并更新至数据库'''
        datestart = self.get_date_start_end(7,1)[0]
        dateend = self.get_date_start_end(7,1)[1]
        sql_select = '''
        SELECT url_id,sum(pv) from ranking_soil_news_daily 
        where src =3 and url_id != 0 and log_date BETWEEN '%s' and '%s'
        group by url_id,src order by sum(pv) desc
        '''%(datestart,dateend)
        self.cur.execute(sql_select)
        data_news_rank = self.cur.fetchall()
        sql_delete='delete from ranking_news_7days where update_date < DATE_SUB(CURDATE(), INTERVAL 3 day)' #清除3天前数据
        self.cur.execute(sql_delete)
        for row in data_news_rank:
            news_id = row[0]
            news_pv = row[1]
            today = datetime.date.today().strftime("%Y-%m-%d")
            sql_update = 'insert into ranking_news_7days(update_date,news_id,pv) values(%s,%s,%s)'
            self.cur.execute(sql_update,(today,news_id,news_pv))
            self.conn.commit()
            #print([today,news_id,news_pv])
        print(sql_select)


