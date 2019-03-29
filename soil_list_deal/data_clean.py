import pymysql

dbconn = pymysql.connect(
    host="******",
    user="******",
    password="******",
    port=3306,
    charset='utf8',
    db='******')

#土地挂牌数据（服务中心与主站）
sql_list='''
SELECT province,city,county,sum(num),sum(area) from

(
SELECT b.name as province,if(c.name=b.name,null,c.name) as city,
if(d.name=c.name,null,d.name) as county,count(*) as num,
round(sum(case mj_type when 1 then mj_num when 2 then mj_num/666.67 end),0) as area
from t_soil_base_info a
LEFT JOIN t_location b on a.loc_province = b.id
LEFT JOIN t_location c on a.loc_city = c.id
LEFT JOIN t_location d on a.loc_county = d.id
where a.svtea in (3,4) and b.is_show =1 and b.`level` =1
group by a.loc_province,a.loc_city,a.loc_county 

union ALL

SELECT b.name as province,if(c.name=b.name,null,c.name) as city,
if(d.name=c.name,null,d.name) as county,count(*) as num,
round(sum(case mj_type when 1 then mj_num when 2 then mj_num/666.67 end),0) as area
from tuliu_v2.tuliu_datas a
LEFT JOIN t_location b on a.loc_province = b.id
LEFT JOIN t_location c on a.loc_city = c.id
LEFT JOIN t_location d on a.loc_county = d.id
where a.svtea in (4,6) and b.is_show =1 and b.`level` =1
group by a.loc_province,a.loc_city,a.loc_county 
)t

group by province,city,county
'''

#土地交易数据（服务中心与主站）
sql_deal='''
SELECT province,city,county,sum(num),sum(area) from

(
SELECT b.name as province,if(c.name=b.name,null,c.name) as city,
if(d.name=c.name,null,d.name) as county,count(*) as num,
round(sum(case mj_type when 1 then mj_num when 2 then mj_num/666.67 end),0) as area
from t_soil_base_info a
LEFT JOIN t_location b on a.loc_province = b.id
LEFT JOIN t_location c on a.loc_city = c.id
LEFT JOIN t_location d on a.loc_county = d.id
where a.svtea =4 and b.is_show =1 and b.`level` =1
group by a.loc_province,a.loc_city,a.loc_county 

union ALL

SELECT b.name as province,if(c.name=b.name,null,c.name) as city,
if(d.name=c.name,null,d.name) as county,count(*) as num,
round(sum(case mj_type when 1 then mj_num when 2 then mj_num/666.67 end),0) as area
from tuliu_v2.tuliu_datas a
LEFT JOIN t_location b on a.loc_province = b.id
LEFT JOIN t_location c on a.loc_city = c.id
LEFT JOIN t_location d on a.loc_county = d.id
where a.svtea =6 and b.is_show =1 and b.`level` =1
group by a.loc_province,a.loc_city,a.loc_county 
)t

group by province,city,county
'''

cur = dbconn.cursor()
cur.execute(sql_list)
data_list=cur.fetchall()
cur.execute(sql_deal)
data_deal=cur.fetchall()
dbconn.close()


dbconn = pymysql.connect(
    host="******",
    user="******",
    password="******",
    port=3306,
    charset='utf8',
    db='******')

sql_drop_list='drop table if exists drill_soil_list'
sql_create_list='''
create table drill_soil_list(
province varchar(50),
city varchar(50),
county varchar(50),
num int(15),
area int(20)
)engine = myisam charset = 'utf8' comment ='土地挂牌数据（用于2级下钻柱图）'
'''


sql_drop_deal='drop table if exists drill_soil_deal'
sql_create_deal='''
create table drill_soil_deal(
province varchar(50),
city varchar(50),
county varchar(50),
num int(15),
area int(20)
)engine = myisam charset = 'utf8' comment ='土地交易数据（用于2级下钻柱图）'
'''

cur=dbconn.cursor()
cur.execute(sql_drop_list)
cur.execute(sql_create_list)
for row in data_list:
    sql_insert_list='insert into drill_soil_list(province,city,county,num,area) values(%s,%s,%s,%s,%s)'
    cur.execute(sql_insert_list,(row[0],row[1],row[2],row[3],row[4]))

cur.execute(sql_drop_deal)
cur.execute(sql_create_deal)
for row in data_deal:
    sql_insert_deal='insert into drill_soil_deal(province,city,county,num,area) values(%s,%s,%s,%s,%s)'
    cur.execute(sql_insert_deal,(row[0],row[1],row[2],row[3],row[4]))
dbconn.commit()
cur.close()
dbconn.close()

