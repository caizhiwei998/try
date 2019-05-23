import datetime
import pandas as pd
import pymysql


class user_rank:
    def __init__(self,datestart,dateend):
        self.datestart = datestart
        self.dateend = dateend
        self.today = datetime.date.today().strftime("%Y-%m-%d")
        self.conn_tuliu = self.dbconn_tuliu_v2()
        self.conn_rank = self.dbconn_ranking_list()
        self.cur_rank = self.conn_rank.cursor()


    def dbconn_tuliu_v2(self):
        '''连接tuliu_v2数据库'''
        dbconn = pymysql.connect(
            host="******",
            user="******",
            password="******",
            db='******',
            port=3306,
            charset='utf8'
        )
        return dbconn


    def close_dbconn_tuliu_v2(self):
        self.conn_tuliu.close()


    def dbconn_ranking_list(self):
        '''排行榜数据库连接'''
        dbconn = pymysql.connect(
            host="******",
            user="******",
            password="******",
            db="******",
            port=3306,
            charset='utf8'
        )
        return dbconn
    
    
    def close_dbconn_ranking_list(self):
        self.cur_rank.close()
        self.conn_rank.close()


    def user_publish_soil_tuliu_score(self):
        '''主站用户发布土地打分（*5）'''
        sql = '''
        SELECT uid,count(*)*5 as score from tuliu_datas where uid !=0 and svtea in(4,6) and 
        date(from_unixtime(create_time)) BETWEEN '%s' and '%s' 
        group by uid
        '''%(self.datestart,self.dateend)
        df = pd.read_sql(sql,self.conn_tuliu)
        return df


    def user_publish_soil_center_score(self):
        '''服务中心用户发布土地打分（*5）'''
        sql = '''
        SELECT uid,count(*)*5 as score from center.t_soil_base_info where uid !=0 and svtea in(3,4) and 
        date(create_time) BETWEEN '%s' and '%s' and source in (4,5,6,8,10) 
        group by uid
        '''%(self.datestart,self.dateend)
        df = pd.read_sql(sql,self.conn_tuliu)
        return df


    def user_publish_need_score(self):
        '''用户发布土地需求打分（*5）'''
        sql = '''
        SELECT pub_person,count(*)*5 as score from s_soil_desired where pub_type = 0 and desired_status in (1,4,5,8) 
        and pub_person !=0 and date(pub_time) BETWEEN '%s' and '%s' GROUP BY pub_person 
        '''%(self.datestart,self.dateend)
        df = pd.read_sql(sql,self.conn_tuliu)
        return df


    def user_clicks_score(self):
        '''土地页用户点击行为(点击查看电话、点击拨打电话、点击IM)打分（*4）'''
        sql = '''
        SELECT uid,sum(if(intertype in (0,2,3),1,0))*4 as score from tuliu_lands_fond_user
        where date(from_unixtime(creat_time)) BETWEEN '%s' and '%s' and uid !=0
        group by uid
        '''%(self.datestart,self.dateend)
        df = pd.read_sql(sql,self.conn_tuliu)
        return df


    def user_visit_score(self):
        '''用户访问土地资讯打分数据'''
        sql = '''
        SELECT log_date,sum(score) as score from ranking_user_visit_score 
        where log_date BETWEEN '%s' and '%s' GROUP BY log_date
        '''%(self.datestart,self.dateend)
        df = pd.read_sql(sql,self.conn_rank)
        return df


    def calculate_score(self):
        '''计算用户整体打分'''
        df_user_fabu_tuliu = self.user_publish_soil_tuliu_score()
        df_user_fabu_center = self.user_publish_soil_center_score()
        df_user_need = self.user_publish_need_score()
        df_user_click = self.user_clicks_score()
        df_user_visit = self.user_visit_score()
        df_concat = pd.concat([df_user_fabu_tuliu,df_user_fabu_center,df_user_need,df_user_click,df_user_visit],axis=0)
        return df_concat


    def sum_score(self):
        '''用户打分求和'''
        df_score = self.calculate_score()
        sum_score = df_score.groupby(['uid'])['score'].sum()
        df_sum_score = pd.DataFrame(sum_score)
        df_sum_score = df_sum_score.reset_index()
        return df_sum_score


    def data_insert(self):
        '''数据传入数据库'''
        df_sum_score = self.sum_score()
        for index,row in df_sum_score.iterrows():
            update_date = str(self.today)
            uid = int(row[0])
            score = int(row[1])
            sql_insert = 'insert into ranking_user_7days(update_date,uid,score) values(%s,%s,%s)'
            self.cur_rank.execute(sql_insert,(update_date,uid,score))
            self.conn_rank.commit()


    def data_delete(self):
        '''清除3天前数据'''
        sql_delete = 'delete from ranking_user_7days where log_date < DATE_SUB(CURDATE(), INTERVAL 3 day)'
        self.cur_rank.execute(sql_delete)
        self.conn_rank.commit()

















