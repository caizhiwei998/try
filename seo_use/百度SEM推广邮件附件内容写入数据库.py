import poplib
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
import datetime
import pandas as pd
import pymysql


def get_start_num(num):
    '''邮件的起始NUM，将小于1的替换为1'''
    if num < 1:
        num = 1
    return num


def get_start_end_date():
    '''读取的邮件的CSV附件的起始日期'''
    dbconn = pymysql.connect(
        host="******",
        user="******",
        password="******",
        db="keyword_analyse",
        port=3306,
        charset='utf8'
    )
    cur=dbconn.cursor()
    sql_select = 'select date_add(max(date),interval 2 day) from sem_keyword_detail'
    cur.execute(sql_select)
    starttime = cur.fetchall()[0][0].strftime('%Y-%m-%d')
    cur.close()
    dbconn.close()
    endtime = str(datetime.datetime.today().strftime('%Y-%m-%d'))
    return [starttime,endtime]


def create_date_list(datestart,dateend):
    '''读取的邮件的CSV附件的日期列表'''
    datestart = datetime.datetime.strptime(datestart, '%Y-%m-%d')
    dateend = datetime.datetime.strptime(dateend, '%Y-%m-%d')
    date_list = []
    while datestart <=dateend:
        # 日期转字符串存入列表
        date_list.append(datestart.strftime('%Y%m%d'))
        # 日期叠加一天
        datestart += datetime.timedelta(days=+1)
    return date_list


def judge_name(file_name,date):
    '''判断是否为当天文件'''
    if file_name == '%s.csv'%(date):
        return True
    else:
        return False


def decode_str(s):
    '''邮件的Subject或者Email中包含的名字都是经过编码后的str，要正常显示，就必须decode'''
    if not s:
        return None
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value


def get_mails(prefix,date):
    '''获取邮件附件，参数输入邮件标题的前缀，及文件日期'''
    host = 'pop.qiye.aliyun.com'
    username = 'seo-no-reply@tuliu.com'
    password = 'seoPassword123'

    server = poplib.POP3(host)
    server.user(username)
    server.pass_(password)
    # 获得邮件 最近20封
    start_num = get_start_num(len(server.list()[1]) - 19)
    end_num = len(server.list()[1]) + 1
    messages = [server.retr(i) for i in range(start_num, end_num)[::-1]]
    messages = [b'\r\n'.join(mssg[1]).decode() for mssg in messages]
    messages = [Parser().parsestr(mssg) for mssg in messages]
    print([start_num, end_num])
    print("====" * 10)

    for message in messages:
        subject = message.get('Subject')
        subject = decode_str(subject)
        # 如果标题匹配
        if subject and subject[:len(prefix)] == prefix:
            value = message.get('From')
            if value:
                hdr, addr = parseaddr(value)
                name = decode_str(hdr)
                value = u'%s <%s>' % (name, addr)
            print("发件人: %s" % value)
            print("标题:%s" % subject)
            for part in message.walk():
                fileName = part.get_filename()
                fileName = decode_str(fileName)
                print(fileName)
                # 保存附件,转为dataframe
                if fileName and judge_name(fileName,date) == True:
                    with open(fileName, 'wb') as fEx:
                        data = part.get_payload(decode=True)
                        fEx.write(data)
                    f = open(fileName,encoding='gbk')
                    df = pd.read_csv(f, header=6)
                    f.close()
                    server.quit()
                    return df


def insert_data(df):
    '''将邮件附件数据写入数据库'''
    dbconn = pymysql.connect(
        host="******",
        user="******",
        password="******",
        db="keyword_analyse",
        port=3306,
        charset='utf8'
    )
    cur=dbconn.cursor()
    for index,row in df.iterrows():
        sql_insert = '''
        insert into sem_keyword_detail(account,date,plan,unit,keyword,`show`,click,cost,click_rate,click_price,page_rank,offer_price,keyword_id)  
        values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) 
        '''
        cur.execute(sql_insert,(row[0],str(row[1]),row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12]))
        dbconn.commit()
        print([row[0],str(row[1]),row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12]])
    cur.close()
    dbconn.close()


if __name__ == '__main__':
    start_date = get_start_end_date()[0]
    end_date = get_start_end_date()[1]
    date_list = create_date_list(start_date,end_date)
    for date in date_list:
        df_sem = get_mails('百度推广统计报告服务', date)
        insert_data(df_sem)
