import pymysql

dbconn=pymysql.connect(
  host="*****",
  user="*****",
  password="*****",
  db="*****",
  port=3306,
  charset='utf8'
 )

#获取最大的消息id
cur=dbconn.cursor()
sql_maxiid="select max(maxiid) from user_im_city_score_maxiid"
cur.execute(sql_maxiid)
maxiid=cur.fetchone()
cur.close()

#获取需计算的用户点击im城市数据
cur=dbconn.cursor()
sql_im="SELECT uid,city,iid from user_im_click_soil where uid != 0 and uid != '' and iid> %s order by iid "%(maxiid)
cur.execute(sql_im)
data_im=cur.fetchall()

if len(data_im)>0: #如果需计算的数据不为空
    #uid,city元祖数据放入空列表中
    list_im=[]
    for row in data_im:
        list_im.append((row[0],row[1]))
    maxiid=data_im[-1][2]#最大消息id
    sql_insert="insert into user_im_city_score_maxiid(maxiid) values(%s)" #最大消息id写入数据库
    cur.execute(sql_insert,(maxiid))
    cur.close()

    i = 0
    #遍历每条im城市数据
    for row in list_im:
        i += 1 #计数
        sql_score = "select uid,city from user_im_city_score where uid=%s" % (row[0]) #获取用户历史数据
        cur = dbconn.cursor()
        cur.execute(sql_score)
        data_score = cur.fetchall()

        if row not in data_score: #如果为新点击的im城市类型数据
            # 将历史im城市打分数据乘以0.9的权重
            sql_loss = "update user_im_city_score set score = score*0.9 where uid='%s'" % (row[0])
            # 将新数据插入打分数据表并打分为1
            sql_add = "insert into user_im_city_score(uid,city,score) values(%s,%s,%s)"
            cur.execute(sql_add, (str(row[0]), str(row[1]), "1"))
            cur.execute(sql_loss)

        elif row in data_score: #如果为之前点击过的im城市类型
            # 将历史im城市打分数据乘以0.9的权重
            sql_loss = "update user_im_city_score set score = score*0.9 where uid='%s'" % (row[0])
            # 将相应的历史数据打分+1
            sql_up = "update user_im_city_score set score = score+1 where uid='%s' and city ='%s'" % (row[0], row[1])
            cur.execute(sql_loss)
            cur.execute(sql_up)
        cur.close()
        print(i) #打印第i条记录

else:
    print('没有需要计算的数据')
dbconn.close()
