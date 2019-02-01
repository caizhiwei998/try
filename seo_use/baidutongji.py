import urllib.request
import urllib.parse
import json
import time
import datetime
import pandas as pd
from sqlalchemy import create_engine

def baidutongji(site_name,site_id,the_days):
    start_date = time.strftime("%Y%m%d", time.localtime())
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    lastday = today - datetime.timedelta(days=the_days)
    end, start = str(yesterday).replace("-", ""), str(lastday).replace("-", "")
    base_url = "https://api.baidu.com/json/tongji/v1/ReportService/getData"
    body = {"header": {"account_type": 1, "password": "tlwseo#2018", "token": "678498e9a72c12573893c40e4bc41aad",
                       "username": "techserv"},
            "body": {"siteId":site_id , "method": "trend/time/a", "start_date": start, "end_date": end,
                     "metrics": "pv_count,visitor_count,ip_count","gran":"day"}} 
    data = bytes(json.dumps(body), 'utf8')
    req = urllib.request.Request(base_url, data)
    response = urllib.request.urlopen(req)
    the_page = response.read()
    result=json.loads(the_page.decode("utf-8"))

    date=result['body']['data'][0]['result']["items"][0]
    values=result['body']['data'][0]['result']["items"][1]

    date_list=[]
    for i in date:
        date_list.append(i[0])

    list_pv=[]
    list_uv=[]
    list_ip=[]
    for j in values:
        list_pv.append(j[0])
        list_uv.append(j[1])
        list_ip.append(j[2])

    date_df=pd.DataFrame(date_list,columns=['date'])
    pv_df=pd.DataFrame(list_pv,columns=[site_name+'_pv'])
    uv_df=pd.DataFrame(list_uv,columns=[site_name+'_uv'])
    ip_df=pd.DataFrame(list_ip,columns=[site_name+'_ip'])
    date_concat=pd.concat([date_df,pv_df,uv_df,ip_df],axis=1).replace('--', 0).sort_values(by="date")
    return date_concat
    
site_list=[['www_tuliu',5703484],['m_tuliu',5792560],['bbs_3s001',8282746],['bbs_tuliu',8282911],
['www_tudinet',9586829],['m_tudinet',10280800],['www_tlw',9854829],['m_tlw',10073017]]

def site_df_concat(site_list,days):
    site_df=[baidutongji(site_list[0][0],site_list[0][1],days).iloc[:,0]]
    for site in site_list:
        site_df.append(baidutongji(site[0],site[1],days).iloc[:,1:])
    site_concat=pd.concat(site_df,axis=1)
    return site_concat
    
site_data_final=site_df_concat(site_list,1462)

conn = create_engine('mysql+pymysql://uesrname:password@host:3306/database?charset=utf8')
#replace替换原数据、append插入数据、fail如果表存在啥也不做
pd.io.sql.to_sql(site_data_final,'baidutongji_tuliu_pv',con=conn,if_exists='append',index=False)  
