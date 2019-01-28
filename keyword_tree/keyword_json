import pymysql
import pandas as pd


dbconn = pymysql.connect(
    host="10.10.66.8",
    user="caizhiwei",
    password="20180803",
    port=3306,
    charset="utf8",
    db="dqytlwork")



sql="""
SELECT  DISTINCT a.curwd as w1,concat(a.subwd,"(",a.wdtyp,")") as w2,
concat(b.subwd,"(",b.wdtyp,")") as w3,
concat(c.subwd,"(",c.wdtyp,")") as w4
from

(SELECT curwd,subwd,wdtyp,layer from words_relation WHERE layer =2 ) a
LEFT JOIN 
(SELECT curwd,subwd,wdtyp from words_relation WHERE layer =3 ) b
on a.subwd=b.curwd
LEFT JOIN 
(SELECT curwd,subwd,wdtyp from words_relation WHERE layer =4 ) c
on b.subwd=c.curwd
where a.curwd in (SELECT DISTINCT curwd from words_relation WHERE layer =2)

"""

#读取数据树结构数据
df_gd=pd.read_sql(sql,dbconn)
df_gd.head(10)



sql2="SELECT subwd,wdtyp from words_relation where layer =1"
df_wdtyp=pd.read_sql(sql2,dbconn)



df_merge=pd.merge(df_gd,df_wdtyp,how='left',left_on='w1',right_on='subwd')
df_merge.head(10)

df_merge['subwd_wdtyp']=df_merge['subwd']+'('+df_merge['wdtyp']+')'
df_merge.head(10)

df_fn=df_merge[['subwd_wdtyp','w2','w3','w4']]
df_fn.columns=['w1','w2','w3','w4']



result = [{"children": [], "name": "土地"}]

# 第一次遍历
word1 = []
for index, row in df_fn.iterrows():
    name = row[0]
    if name not in word1:
        word1.append(name)
        node = {"children": [], "name": name}
        result[0]["children"].append(node)



# 第二次遍历
word2 = []
for index, row in df_fn.iterrows():
    name1 = row[0]
    name2 = row[1]
    if name2 not in word2 and name2 != None:
        word2.append(name2)
        node = {"children": [], "name": name2}
        for i in result[0]["children"]:
            if i["name"] == name1:
                i["children"].append(node)
                break


# 第三次遍历
word3 = []
for index, row in df_fn.iterrows():
    name1 = row[0]
    name2 = row[1]
    name3 = row[2]
    if name3 not in word3 and name3 != None:
        word3.append(name3)
        node = {"children": [], "name": name3}
        for i in result[0]["children"]:
            if i["name"] == name1:
                for j in i["children"]:
                    if j["name"] == name2:
                        j["children"].append(node)
                        break


# 第四次遍历
word4 = []
for index, row in df_fn.iterrows():
    name1 = row[0]
    name2 = row[1]
    name3 = row[2]
    name4 = row[3]
    if name4 not in word4 and name4 != None:
        word4.append(name4)
        node = {"children": [], "name": name4}
        for i in result[0]["children"]:
            if i["name"] == name1:
                for j in i["children"]:
                    if j["name"] == name2:
                        for k in j["children"]:
                            if k["name"] == name3:
                                k["children"].append(node)
                                break



conn = pymysql.connect(
        host="10.10.66.8",
        user="caizhiwei",
        password="20180803",
        port=3306,
        charset="utf8",
        db="dqytlwork")

#上传JSON数据
cursor = conn.cursor()
sql2 = "INSERT INTO words_relation_json(id,json) VALUES (%s,%s)"
cursor.execute(sql2,('1',str(result)))
conn.commit()


