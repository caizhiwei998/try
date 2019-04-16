import datetime
import pymysql
import re

class sv_soil_pv_web:

    def __init__(self,datestart,dateend,nglog_table):
        '''传入起始日期及表名'''
        self.nglog_table= nglog_table
        self.date_list = self.create_date_list(datestart,dateend)
        self.conn_nglog=self.dbconn_nglog()
        self.cur_nglog=self.conn_nglog.cursor()
        self.conn_center=self.dbconn_center()
        self.cur_center=self.conn_center.cursor()


    def dbconn_nglog(self):
        '''日志数据库连接'''
        dbconn = pymysql.connect(
            host="******",
            user="******",
            password="******",
            db="******",
            port=3306,
            charset='utf8'
        )
        return dbconn


    def dbconn_center(self):
        '''服务中心数据库连接'''
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
        self.conn_nglog.close()
        self.cur_nglog.close()
        self.conn_center.close()
        self.cur_nglog.close()


    def create_date_list(self,datestart,dateend):
        '''建立日期列表'''
        # 转为日期格式
        datestart=datetime.datetime.strptime(datestart,'%Y-%m-%d')
        dateend=datetime.datetime.strptime(dateend,'%Y-%m-%d')
        date_list = []
        date_list.append(datestart.strftime('%Y-%m-%d'))
        while datestart<dateend:
            # 日期叠加一天
            datestart+=datetime.timedelta(days=+1)
            # 日期转字符串存入列表
            date_list.append(datestart.strftime('%Y-%m-%d'))
        return date_list


    def get_sview_data(self):
        '''获取服务中心土地[url,date]列表'''
        for date in self.date_list:
            sql= '''
            SELECT url,case sitetype when 'tuliu_pc' then 'pc' when 'tuliu_wap' then 'wap' end
            from %s where url REGEXP('s-view-') and time BETWEEN '%s 00:00:00' and '%s 23:59:59'
            and uag != 'mozilla/5.0 (compatible; baiduspider-render/2.0; +http://www.baidu.com/search/spider.html)'            
            ''' % (self.nglog_table,date, date)
            self.cur_nglog.execute(sql)
            url_tuple = self.cur_nglog.fetchall()
            for url in url_tuple:
                url_date_list = [url[0],url[1],date]
                print(url_date_list)
                yield  url_date_list #[url,src,date]


    def get_soilid_date(self):
        '''获取土地id'''
        pattern = re.compile(r's-view-(\d+)')
        for url_date in self.get_sview_data():
            m_url = pattern.search(url_date[0])
            if m_url != None:
                soil_id = m_url.group(1)
                sid_date_list=[soil_id,url_date[1],url_date[2]]
                yield sid_date_list #[soil_id,src,date]


    def get_svid(self):
        '''获取服务中心id'''
        for sid_date in self.get_soilid_date():
            sql='SELECT sv_id from t_service_soil where soil_id = %s and enabled =1'%(sid_date[0])
            self.cur_center.execute(sql)
            sv_id=self.cur_center.fetchall()
            if len(sv_id)>0:
                svid_date_list=[sv_id[0][0],sid_date[1],sid_date[2]]
                yield svid_date_list #[sv_id,src,date]


    def update_sv_data(self):
        '''更新服务中心土地流量数据'''
        i=0
        for svid_date in self.get_svid():
            sv_id = svid_date[0]
            src = svid_date[1]
            date = svid_date[2]
            i+=1
            print('NO'+str(i)+'_sv_id='+str(sv_id))
            sql_find_sv = "select sv_id from sv_data_analyse.sv_soilpv_daily " \
                          "where date = '%s' and sv_id = %s and src = '%s' "%(date,sv_id,src)
            self.cur_nglog.execute(sql_find_sv)
            find_sv=self.cur_nglog.fetchall()
            if len(find_sv)>0:
                sql_update_sv="update sv_data_analyse.sv_soilpv_daily set soil_pv=soil_pv+1 " \
                              "where date='%s' and sv_id=%s and src = '%s' "%(date,sv_id,src)
                self.cur_nglog.execute(sql_update_sv)
            else:
                sql_insert_sv="insert into sv_data_analyse.sv_soilpv_daily values(%s,%s,'1',%s)"
                self.cur_nglog.execute(sql_insert_sv,(date,sv_id,src))



class sv_soil_pv_app(sv_soil_pv_web):

    def __init__(self,datestart,dateend,nglog_table):
        sv_soil_pv_web.__init__(self, datestart, dateend, nglog_table)


    def get_sview_data(self):
        '''获取土地[soil_id-(1,2),date]列表(APP日志中-1为服务中心-2为主站)'''
        for date in self.date_list:
            sql= '''
            SELECT qt,dk from %s where time BETWEEN '%s 00:00:00' and '%s 23:59:59' and xw= '浏览-土地供应详情'           
            ''' % (self.nglog_table,date, date)
            self.cur_nglog.execute(sql)
            url_tuple = self.cur_nglog.fetchall()
            for qt in url_tuple:
                qt_date_list = [qt[0],qt[1],date]
                print(qt_date_list)
                yield  qt_date_list #[soil_id-(1,2),src,date]


    def get_soilid_date(self):
        '''获取土地id'''
        pattern = re.compile(r'(\d+)-(\d+)')
        for qt_date in self.get_sview_data():
            m_qt = pattern.search(qt_date[0])
            if m_qt != None:
                if m_qt.group(2) == '1':
                    soil_id = m_qt.group(1)
                    sid_date_list=[soil_id,qt_date[1],qt_date[2]]
                    yield sid_date_list #[soil_id,src,date]


if __name__ == '__main__':
    web03=sv_soil_pv_web('2019-03-01','2019-03-31','nglog_pcwap_201903')
    web03.update_sv_data()
    web03.close_dbconn()

    app03=sv_soil_pv_app('2019-03-01','2019-03-31','nglog_app')
    app03.update_sv_data()
    app03.close_dbconn()









