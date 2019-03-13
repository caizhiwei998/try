SELECT t1.id as country_id,t1.name as country,t2.id as province_id,t2.name as province,
t3.id as city_id,t3.name as city,t4.id as county_id,t4.name as county

from (SELECT id,fuid,name from t_location where is_show=1) t1 

LEFT JOIN (SELECT id,fuid,name from t_location where is_show=1) t2  on t1.id=t2.fuid 

LEFT JOIN (SELECT id,fuid,name from t_location where is_show=1) t3  on t2.id=t3.fuid

LEFT JOIN (SELECT id,fuid,name from t_location where is_show=1) t4  on t3.id=t4.fuid

where t1.id =3253 #id为中国的id
