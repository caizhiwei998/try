import numpy as np
import pandas as pd
import pymysql
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


def get_kw_base_df():
    '''获取近7天关键词基础数据'''
    dbconn = pymysql.connect(
        host="******",
        user="******",
        password="******",
        db="******",
        port=3306,
        charset='utf8'
    )
    sql = '''
    SELECT a.keyword,
    b.min_rank as rank1,c.min_rank as rank2,d.min_rank as rank3,
    e.min_rank as rank4,f.min_rank as rank5,g.min_rank as rank6,h.min_rank as rank7,
    b.max_show as show1,c.max_show as show2,d.max_show as show3,
    e.max_show as show4,f.max_show as show5,g.max_show as show6,h.max_show as show7,
    b.max_click as click1,c.max_click as click2,d.max_click as click3,
    e.max_click as click4,f.max_click as click5,g.max_click as click6,h.max_click as click7
    from 

    (SELECT DISTINCT keyword from sem_keyword_detail where date >= DATE_SUB(CURDATE(),INTERVAL 7 DAY)) a

    LEFT JOIN 
    (SELECT keyword,max(`show`) as max_show,max(click) as max_click,case min(page_rank) when 0 then null else min(page_rank) end as min_rank
    FROM sem_keyword_detail where date = DATE_SUB(CURDATE(),INTERVAL 1 DAY) GROUP BY keyword) b
    ON a.keyword = b.keyword

    LEFT JOIN 
    (SELECT keyword,max(`show`) as max_show,max(click) as max_click,case min(page_rank) when 0 then null else min(page_rank) end as min_rank
    FROM sem_keyword_detail where date = DATE_SUB(CURDATE(),INTERVAL 2 DAY) GROUP BY keyword) c
    ON a.keyword = c.keyword

    LEFT JOIN 
    (SELECT keyword,max(`show`) as max_show,max(click) as max_click,case min(page_rank) when 0 then null else min(page_rank) end as min_rank
    FROM sem_keyword_detail where date = DATE_SUB(CURDATE(),INTERVAL 3 DAY) GROUP BY keyword) d
    ON a.keyword = d.keyword

    LEFT JOIN 
    (SELECT keyword,max(`show`) as max_show,max(click) as max_click,case min(page_rank) when 0 then null else min(page_rank) end as min_rank
    FROM sem_keyword_detail where date = DATE_SUB(CURDATE(),INTERVAL 4 DAY) GROUP BY keyword) e
    ON a.keyword = e.keyword

    LEFT JOIN 
    (SELECT keyword,max(`show`) as max_show,max(click) as max_click,case min(page_rank) when 0 then null else min(page_rank) end as min_rank
    FROM sem_keyword_detail where date = DATE_SUB(CURDATE(),INTERVAL 5 DAY) GROUP BY keyword) f
    ON a.keyword = f.keyword

    LEFT JOIN 
    (SELECT keyword,max(`show`) as max_show,max(click) as max_click,case min(page_rank) when 0 then null else min(page_rank) end as min_rank
    FROM sem_keyword_detail where date = DATE_SUB(CURDATE(),INTERVAL 6 DAY) GROUP BY keyword) g
    ON a.keyword = g.keyword

    LEFT JOIN 
    (SELECT keyword,max(`show`) as max_show,max(click) as max_click,case min(page_rank) when 0 then null else min(page_rank) end as min_rank
    FROM sem_keyword_detail where date = DATE_SUB(CURDATE(),INTERVAL 7 DAY) GROUP BY keyword) h
    ON a.keyword = h.keyword
    '''
    df = pd.read_sql(sql, dbconn)
    return df


def calculate_show_click_trans(df):
    '''计算关键词排名升降'''
    df['rank1-2'] = df['rank2'] - df['rank1']
    df['rank1/2'] = df['rank2'] / df['rank1'] - 1
    return df


def date_ls():
    '''获取前7天日期'''
    date1 = str((datetime.date.today() + datetime.timedelta(days=-1)).strftime("%Y%m%d"))
    date2 = str((datetime.date.today() + datetime.timedelta(days=-2)).strftime("%Y%m%d"))
    date3 = str((datetime.date.today() + datetime.timedelta(days=-3)).strftime("%Y%m%d"))
    date4 = str((datetime.date.today() + datetime.timedelta(days=-4)).strftime("%Y%m%d"))
    date5 = str((datetime.date.today() + datetime.timedelta(days=-5)).strftime("%Y%m%d"))
    date6 = str((datetime.date.today() + datetime.timedelta(days=-6)).strftime("%Y%m%d"))
    date7 = str((datetime.date.today() + datetime.timedelta(days=-7)).strftime("%Y%m%d"))
    ls = [date1,date2,date3,date4,date5,date6,date7]
    return ls


def rank_days_from(df):
    '''返回日环比dataframe'''
    df_rank_days_from = df[['keyword','show1','show2','click1','click2','rank1','rank2','rank1-2','rank1/2']]
    df_rank_days_from = df_rank_days_from[(df_rank_days_from['rank1'] > 0) & (df_rank_days_from['rank2'] > 0)]
    date1 = date_ls()[0]
    date2 = date_ls()[1]
    df_rank_days_from.columns=['关键词','展现'+date1,'展现'+date2,'点击'+date1,'点击'+date2,'排名'+date1,'排名'+date2,'排名涨跌','排名环比']
    df_rank_days_from[u'排名环比'] = df_rank_days_from[u'排名环比'].apply(lambda x: format(x, '.2%'))
    return df_rank_days_from


def no_rank_7days(df):
    '''返回7天无排名关键词dataframe'''
    df_no_rank_7days = df[np.isnan(df['rank1']) & np.isnan(df['rank2']) & np.isnan(df['rank3']) & np.isnan(df['rank4'])
                          & np.isnan(df['rank5']) & np.isnan(df['rank6']) & np.isnan(df['rank7'])]
    df_no_rank_7days = df_no_rank_7days[['keyword','show1','show2','show3','show4','show5','show6','show7'
        ,'click1','click2','click3','click4','click5','click6','click7']]
    date1 = date_ls()[0]
    date2 = date_ls()[1]
    date3 = date_ls()[2]
    date4 = date_ls()[3]
    date5 = date_ls()[4]
    date6 = date_ls()[5]
    date7 = date_ls()[6]
    df_no_rank_7days.columns = ['关键词','展现'+date1,'展现'+date2,'展现'+date3,'展现'+date4,'展现'+date5,'展现'+date6,'展现'+date7
        ,'点击'+date1,'点击'+date2,'点击'+date3,'点击'+date4,'点击'+date5,'点击'+date6,'点击'+date7]
    return df_no_rank_7days


def no_rank_yesterday(df):
    '''返回昨日无排名但前7天有排名的关键词dataframe'''
    df_no_rank_yesterday = df[np.isnan(df['rank1'])&((df['rank2']>0)|(df['rank3']>0)|(df['rank4']>0)|(df['rank5']>0)|(df['rank6']>0)|(df['rank7']>0))]
    df_no_rank_yesterday = df_no_rank_yesterday[['keyword','show1','click1','rank1','rank2','rank3','rank4','rank5','rank6','rank7']]
    date1 = date_ls()[0]
    date2 = date_ls()[1]
    date3 = date_ls()[2]
    date4 = date_ls()[3]
    date5 = date_ls()[4]
    date6 = date_ls()[5]
    date7 = date_ls()[6]
    df_no_rank_yesterday.columns = ['关键词','展现'+date1,'点击'+date1,'排名'+date1,'排名'+date2,'排名'+date3,'排名'+date4,'排名'+date5,'排名'+date6,'排名'+date7]
    return df_no_rank_yesterday


def sent_report(file1,file2,file3,name1,name2,name3):
    # 第三方 SMTP 服务
    mail_host = "smtp.qiye.aliyun.com"  # 设置服务器
    mail_user = "******@tuliu.com"  # 用户名
    mail_pass = "******"  # 口令

    sender = '******@tuliu.com'
    receivers = ['cai@******.com','******@******.com']  # 接收邮件

    message = MIMEMultipart()
    message['From'] = Header("数据部自动发送", 'utf-8')  # 发送者
    message['To'] = Header("SEM", 'utf-8')  # 接收者

    subject = 'SEM关键词日报[%s]'%(date_ls()[0])  # 标题
    message['Subject'] = Header(subject, 'utf-8')

    #邮件正文内容
    message.attach(MIMEText('数据详情见附件，数据来源于百度SEM推广每日自动发送的邮件。日环比数据为昨天与前天排名对比，并且2天都有排名。昨日无排名数据为昨天没有排名但在近7天有排名的关键词明细。近7日无排名数据为在近7天都没有排名的关键词明细。'
                            , 'plain', 'utf-8'))

    # 构造附件1
    att1 = MIMEText(open(file1, 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1.add_header("Content-Disposition", "attachment", filename=("gbk", "", name1))
    message.attach(att1)

    # 构造附件2
    att2 = MIMEText(open(file2, 'rb').read(), 'base64', 'utf-8')
    att2["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att2.add_header("Content-Disposition", "attachment", filename=("gbk", "", name2))
    message.attach(att2)

    # 构造附件3
    att3 = MIMEText(open(file3, 'rb').read(), 'base64', 'utf-8')
    att3["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att3.add_header("Content-Disposition", "attachment", filename=("gbk", "", name3))
    message.attach(att3)

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        smtpObj.close()
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")


if  __name__ == '__main__':
    df_kw_base = get_kw_base_df()
    df_all = calculate_show_click_trans(df_kw_base)
    df_rank_days_from = rank_days_from(df_all)
    df_no_rank_7days = no_rank_7days(df_all)
    df_no_rank_yesterday = no_rank_yesterday(df_all)

    today = date_ls()[0]
    df_rank_days_from.to_csv(r'/home/caizhiwei/mypython/baidu_keyword/sem_report/sem_keyword_rank_days_from_%s.csv'%(today),index=False,encoding='gbk')
    df_no_rank_yesterday.to_csv(r'/home/caizhiwei/mypython/baidu_keyword/sem_report/sem_keyword_no_rank_yesterday_%s.csv'%(today),index=False,encoding='gbk')
    df_no_rank_7days.to_csv(r'/home/caizhiwei/mypython/baidu_keyword/sem_report/sem_keyword_no_rank_7days_%s.csv'%(today),index=False,encoding='gbk')

    file1 = '/home/caizhiwei/mypython/baidu_keyword/sem_report/sem_keyword_rank_days_from_%s.csv'%(today)
    file2 = '/home/caizhiwei/mypython/baidu_keyword/sem_report/sem_keyword_no_rank_yesterday_%s.csv'%(today)
    file3 = '/home/caizhiwei/mypython/baidu_keyword/sem_report/sem_keyword_no_rank_7days_%s.csv'%(today)
    name1 = 'sem关键词日环比数据_%s.csv'%(today)
    name2 = 'sem关键词昨日无排名数据_%s.csv'%(today)
    name3 = 'sem关键词近7日无排名数据_%s.csv'%(today)
    sent_report(file1, file2, file3,name1,name2,name3)
