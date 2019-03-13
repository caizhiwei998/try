#建表
drop  table  IF  EXISTS  user_rank;
CREATE  TABLE  `user_rank`  (
    `uid`  int(12)  DEFAULT  NULL  COMMENT  '3s002的用户id',
    `reg_date`  datetime  DEFAULT  NULL  COMMENT  '用户注册时间',
    `reg_days`  int(6)  DEFAULT  NULL  COMMENT  '用户注册至今多少天',
    `rank`  int(12)  DEFAULT  NULL  COMMENT  '用户注册排名',
    `percent`  varchar(10)  DEFAULT  NULL  COMMENT  '注册超多少用户百分比',
    KEY  `uid`  (`uid`)
)  ENGINE=MyISAM  DEFAULT  CHARSET=utf8  COMMENT='用户注册排名表';

#设置变量
set  @total:=0;#排名计数
set  @max_rank=(SELECT  count(uid)  from  3s002.pre_ucenter_members  );#最大排名数

#插入查询数据
insert  into    user_rank(uid,reg_date,reg_days,rank,percent)  
(SELECT  uid,from_unixtime(regdate)  as  reg_date,
to_days(CURDATE())-to_days(from_unixtime(regdate))  as  reg_days,
@total:=@total+1  as  rank,  
concat(TRUNCATE  (@percent:=(1-@total/@max_rank)  *  100,  2),'%')  as  percent  
from  3s002.pre_ucenter_members  where  year(from_unixtime(regdate))  <=2018  ORDER  BY  regdate);


