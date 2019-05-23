#!/bin/bash
#提取日志数据
~/Python-3.6.4/python36 ~/mypython/ranking_list/run_parse_ranking_soil_news.py
#计算土地资讯排名
~/Python-3.6.4/python36 ~/mypython/ranking_list/run_get_soil_news_rank.py
#计算用户访问土地资讯打分
~/Python-3.6.4/python36 ~/mypython/ranking_list/run_parse_user_visit.py
#计算用户活跃排名
~/Python-3.6.4/python36 ~/mypython/ranking_list/run_get_user_rank.py
