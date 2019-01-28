import pandas as pd
import arrow
from pyecharts import Pie,Bar,Line,Overlap,Map,WordCloud


def fabu_diqu(conn,days,width,height):
    sql_fabu_diqu = "select name,count,mj from kanban_fabu_diqu where create_date= (select max(create_date) from kanban_fabu_diqu)"
    data_fabu_diqu = pd.read_sql(sql_fabu_diqu,conn)

    fabu_diqu_name = list(data_fabu_diqu.iloc[:, 0])
    fabu_diqu_mj = list(data_fabu_diqu.iloc[:, 2])
    fabu_diqu_count = list(data_fabu_diqu.iloc[:, 1])

    fabu_diqu_title = str(arrow.now().shift(days=days,months=-1).year) + '年' + str(
        arrow.now().shift(days=days,months=-1).month) + '月土流网发布土地区域分布'
    fabu_diqu_bar = Bar(fabu_diqu_title)
    fabu_diqu_bar.add("面积（亩）", fabu_diqu_name, fabu_diqu_mj, xaxis_interval=0, xaxis_rotate=90)
    fabu_diqu_line = Line()
    fabu_diqu_line.add("宗数", fabu_diqu_name, fabu_diqu_count, xaxis_interval=0, xaxis_rotate=90)

    fabu_diqu_overlap = Overlap(height=height, width=width)
    fabu_diqu_overlap.add(fabu_diqu_bar)
    fabu_diqu_overlap.add(fabu_diqu_line, yaxis_index=1, is_add_yaxis=True)
    fabu_diqu_overlap.render()

    return fabu_diqu_overlap


def fabu_map(conn,width,height):
    sql_fabu_map = "select name,count,mj from kanban_fabu_map where create_date= (select max(create_date) from kanban_fabu_map)"
    data_fabu_map = pd.read_sql(sql_fabu_map, conn)

    fabu_map_name = list(data_fabu_map.iloc[:, 0])
    fabu_map_count = list(data_fabu_map.iloc[:, 1])

    fabu_map_map = Map("土流网最近1年土地发布数区域分布热力图（单位：宗）", width=width, height=height)
    fabu_map_map.add("", fabu_map_name, fabu_map_count, maptype="china", is_visualmap=True,
                     visual_range=[0, data_fabu_map.iloc[0, 1]], visual_range_color=['#FAF0E6', '#FE9A2E', '#FE642E'],
                     is_label_show=True)
    fabu_map_map.render()
    return fabu_map_map


def fabu_type(conn,days,width,height,zs_mj):
    sql_fabu_type = "select type,count,mj from kanban_fabu_type where create_date= (select max(create_date) from kanban_fabu_type)"
    data_fabu_type = pd.read_sql(sql_fabu_type,conn)

    date_fabu_type_count = data_fabu_type.sort_values('count', ascending=False)
    date_fabu_type_mj = data_fabu_type.sort_values('mj', ascending=False)

    fabu_type_name1 = list(date_fabu_type_count.iloc[:, 0])
    fabu_type_count1 = list(date_fabu_type_count.iloc[:, 1])
    fabu_type_name2 = list(date_fabu_type_mj.iloc[:, 0])
    fabu_type_mj2 = list(date_fabu_type_mj.iloc[:, 2])

    if zs_mj=='zs':
        fabu_type_title1 = str(arrow.now().shift(days=days,months=-1).year) + '年' + str(
            arrow.now().shift(days=days,months=-1).month) + '月土流网发布土地类型宗数占比'
        fabu_type_pie1 = Pie(fabu_type_title1, title_pos='center', width=width, height=height)
        fabu_type_pie1.add("", fabu_type_name1, fabu_type_count1, rosetype='radius', radius=[25, 50],
                           label_text_color=None,
                           is_label_show=True, is_legend_show=False, legend_orient='vertical',
                           legend_pos='left')
        fabu_type_pie1.render()
        return fabu_type_pie1

    elif zs_mj=='mj':
        fabu_type_title2 = str(arrow.now().shift(days=days,months=-1).year) + '年' + str(
            arrow.now().shift(days=days,months=-1).month) + '月土流网发布土地类型面积占比'
        fabu_type_pie2 = Pie(fabu_type_title2, title_pos='center', width=width, height=height)
        fabu_type_pie2.add("", fabu_type_name2, fabu_type_mj2, rosetype='radius', radius=[25, 50],
                           label_text_color=None,
                           is_label_show=True, is_legend_show=False, legend_orient='vertical',
                           legend_pos='left')
        fabu_type_pie2.render()
        return fabu_type_pie2


def fabu_liuzhuan(conn,days,width,height,zs_mj):
    sql_fabu_liuzhuan="select liuzhuan,count,mj from kanban_fabu_liuzhuan where create_date= (select max(create_date) from kanban_fabu_liuzhuan)"
    data_fabu_liuzhuan=pd.read_sql(sql_fabu_liuzhuan,conn)

    data_fabu_liuzhuan_count=data_fabu_liuzhuan.sort_values('count',ascending=False)
    data_fabu_liuzhuan_mj=data_fabu_liuzhuan.sort_values('mj',ascending=False)

    fabu_liuzhuan_name1=list(data_fabu_liuzhuan_count.iloc[:,0])
    fabu_liuzhuan_count1=list(data_fabu_liuzhuan_count.iloc[:,1])
    fabu_liuzhuan_name2=list(data_fabu_liuzhuan_mj.iloc[:,0])
    fabu_liuzhuan_mj2=list(data_fabu_liuzhuan_mj.iloc[:,2])

    if zs_mj=='zs':
        fabu_liuzhuan_title1=str(arrow.now().shift(days=days,months=-1).year)+'年'+str(
            arrow.now().shift(days=days,months=-1).month)+'月土流网发布土地流转类型宗数占比'
        fabu_liuzhuan_pie1 = Pie(fabu_liuzhuan_title1, title_pos='center', width=width, height=height)
        fabu_liuzhuan_pie1.add("",fabu_liuzhuan_name1, fabu_liuzhuan_count1, radius=[25,50], label_text_color=None,
                is_label_show=True,is_legend_show=False, legend_orient='vertical',
                legend_pos='left')
        fabu_liuzhuan_pie1.render()
        return fabu_liuzhuan_pie1

    elif zs_mj=='mj':
        fabu_liuzhuan_title2 = str(arrow.now().shift(days=days,months=-1).year) + '年' + str(
            arrow.now().shift(days=days,months=-1).month) + '月土流网发布土地流转类型面积占比'
        fabu_liuzhuan_pie2 = Pie(fabu_liuzhuan_title2, title_pos='center', width=width, height=height)
        fabu_liuzhuan_pie2.add("", fabu_liuzhuan_name2, fabu_liuzhuan_mj2, radius=[25, 50], label_text_color=None,
                               is_label_show=True, is_legend_show=False, legend_orient='vertical',
                               legend_pos='left')
        fabu_liuzhuan_pie2.render()
        return fabu_liuzhuan_pie2


def fabu_size(conn,days,width,height):
    sql_fabu_size = "select dikuai,count,mj from kanban_fabu_dikuai where create_date= (select max(create_date) from kanban_fabu_dikuai)"
    data_fabu_size = pd.read_sql(sql_fabu_size, conn)

    fabu_size_title = str(arrow.now().shift(days=days,months=-1).year) + '年' + str(
        arrow.now().shift(days=days,months=-1).month) + '月土流网各规模农业用地发布量（宗）'
    fabu_size_type = list(data_fabu_size.iloc[:, 0])
    fabu_size_count = list(data_fabu_size.iloc[:, 2])

    fabu_size_bar = Bar(fabu_size_title, title_pos='center', width=width, height=height)
    fabu_size_bar.add("", fabu_size_type, fabu_size_count, is_stack=True)
    fabu_size_bar.render()
    return fabu_size_bar


def fabu_nianxian(conn,days,width,height):
    sql_fabu_nianxian="select type,year from kanban_fabu_nianxian where create_date= (select max(create_date) from kanban_fabu_nianxian)"
    data_fabu_nianxian=pd.read_sql(sql_fabu_nianxian,conn)

    fabu_nianxian_type = list(data_fabu_nianxian.iloc[:,0])
    fabu_nianxian_year= list(data_fabu_nianxian.iloc[:,1])
    fabu_nianxian_title=str(arrow.now().shift(days=days,months=-1).year)+'年'+str(
        arrow.now().shift(days=days,months=-1).month)+'月土流网各土地类型平均流转年限'
    fabu_nianxian_bar = Bar(fabu_nianxian_title, title_pos='center', width=width, height=height)
    fabu_nianxian_bar.add("",fabu_nianxian_type,fabu_nianxian_year, is_stack=True,xaxis_interval=0)
    fabu_nianxian_bar.render()
    return fabu_nianxian_bar


def fabu_label(conn,days,width,height):
    sql_fabu_label = "select name,count from kanban_fabu_label where create_date= (select max(create_date) from kanban_fabu_label)"
    data_fabu_label = pd.read_sql(sql_fabu_label, conn)

    fabu_label_name = list(data_fabu_label.iloc[:, 0])
    fabu_label_count = list(data_fabu_label.iloc[:, 1])

    fabu_label_title = str(arrow.now().shift(days=days,months=-1).year) + '年' + str(
        arrow.now().shift(days=days,months=-1).month) + '月土流网发布土地标签词云图'
    fabu_label_wordcloud = WordCloud(fabu_label_title, width=width, height=height, title_pos='center')
    fabu_label_wordcloud.add("", fabu_label_name, fabu_label_count, shape="circle")
    fabu_label_wordcloud.render()
    return fabu_label_wordcloud





def jiaoyi_map(conn,width,height):
    sql_jiaoyi_map = "select name,count,mj from kanban_jiaoyi_map where create_date= (select max(create_date) from kanban_jiaoyi_map)"
    data_jiaoyi_map = pd.read_sql(sql_jiaoyi_map, conn)

    jiaoyi_map_name = list(data_jiaoyi_map.iloc[:, 0])
    jiaoyi_map_count = list(data_jiaoyi_map.iloc[:, 1])

    jiaoyi_map_map = Map("土流网最近1年土地交易数区域分布热力图（单位：宗）", width=width, height=height)
    jiaoyi_map_map.add("", jiaoyi_map_name, jiaoyi_map_count, maptype="china", is_visualmap=True,
                       visual_range=[0, data_jiaoyi_map.iloc[0, 1]],
                       visual_range_color=['#FAF0E6', '#FE9A2E', '#FE642E'], is_label_show=True)
    jiaoyi_map_map.render()
    return jiaoyi_map_map


def jiaoyi_diqu(conn,days,width,height):
    sql_jiaoyi_diqu = "select name,count,mj from kanban_jiaoyi_diqu where create_date= (select max(create_date) from kanban_jiaoyi_diqu)"
    data_jiaoyi_diqu = pd.read_sql(sql_jiaoyi_diqu, conn)

    jiaoyi_diqu_name = list(data_jiaoyi_diqu.iloc[:, 0])
    jiaoyi_diqu_mj = list(data_jiaoyi_diqu.iloc[:, 2])
    jiaoyi_diqu_count = list(data_jiaoyi_diqu.iloc[:, 1])
    jiaoyi_diqu_title = str(arrow.now().shift(days=days,months=-1).year) + '年' + str(
        arrow.now().shift(days=days,months=-1).month) + '月土流网交易区域分布'
    jiaoyi_diqu_bar = Bar(jiaoyi_diqu_title)
    jiaoyi_diqu_bar.add("面积（亩）", jiaoyi_diqu_name, jiaoyi_diqu_mj, xaxis_interval=0, xaxis_rotate=90)
    jiaoyi_diqu_line = Line()
    jiaoyi_diqu_line.add("宗数", jiaoyi_diqu_name, jiaoyi_diqu_count, xaxis_interval=0, xaxis_rotate=90)

    jiaoyi_diqu_overlap = Overlap(height=height, width=width)
    jiaoyi_diqu_overlap.add(jiaoyi_diqu_bar)
    jiaoyi_diqu_overlap.add(jiaoyi_diqu_line, yaxis_index=1, is_add_yaxis=True)
    jiaoyi_diqu_overlap.render()

    return jiaoyi_diqu_overlap


def jiaoyi_type(conn,days,width,height,zs_mj):
    sql_jiaoyi_type = "select type,count,mj from kanban_jiaoyi_type where create_date= (select max(create_date) from kanban_jiaoyi_type)"
    data_jiaoyi_type = pd.read_sql(sql_jiaoyi_type, conn)

    date_jiaoyi_type_count = data_jiaoyi_type.sort_values('count', ascending=False)
    date_jiaoyi_type_mj = data_jiaoyi_type.sort_values('mj', ascending=False)

    jiaoyi_type_name1 = list(date_jiaoyi_type_count.iloc[:, 0])
    jiaoyi_type_count1 = list(date_jiaoyi_type_count.iloc[:, 1])
    jiaoyi_type_name2 = list(date_jiaoyi_type_mj.iloc[:, 0])
    jiaoyi_type_mj2 = list(date_jiaoyi_type_mj.iloc[:, 2])

    if zs_mj == 'zs':
        jiaoyi_type_title1 = str(arrow.now().shift(days=days,months=-1).year) + '年' + str(
            arrow.now().shift(days=days,months=-1).month) + '月土流网交易土地类型宗数占比'
        jiaoyi_type_pie1 = Pie(jiaoyi_type_title1, title_pos='center', width=width, height=height)
        jiaoyi_type_pie1.add("", jiaoyi_type_name1, jiaoyi_type_count1, rosetype='radius', radius=[25, 50],
                             label_text_color=None,
                             is_label_show=True, is_legend_show=False, legend_orient='vertical',
                             legend_pos='left')
        jiaoyi_type_pie1.render()
        return jiaoyi_type_pie1

    elif zs_mj == 'mj':
        jiaoyi_type_title2 = str(arrow.now().shift(days=days,months=-1).year) + '年' + str(
            arrow.now().shift(days=days,months=-1).month) + '月土流网交易土地类型面积占比'
        jiaoyi_type_pie2 = Pie(jiaoyi_type_title2, title_pos='center', width=width, height=height)
        jiaoyi_type_pie2.add("", jiaoyi_type_name2, jiaoyi_type_mj2, rosetype='radius', radius=[25, 50],
                             label_text_color=None,
                             is_label_show=True, is_legend_show=False, legend_orient='vertical',
                             legend_pos='left')
        jiaoyi_type_pie2.render()
        return jiaoyi_type_pie2


def jiaoyi_liuzhuan(conn,days,width,height,zs_mj):
    sql_jiaoyi_liuzhuan = "select liuzhuan,count,mj from kanban_jiaoyi_liuzhuan where create_date= (select max(create_date) from kanban_jiaoyi_liuzhuan)"
    data_jiaoyi_liuzhuan = pd.read_sql(sql_jiaoyi_liuzhuan, conn)

    data_jiaoyi_liuzhuan_count = data_jiaoyi_liuzhuan.sort_values('count', ascending=False)
    data_jiaoyi_liuzhuan_mj = data_jiaoyi_liuzhuan.sort_values('mj', ascending=False)

    jiaoyi_liuzhuan_name1 = list(data_jiaoyi_liuzhuan_count.iloc[:, 0])
    jiaoyi_liuzhuan_count1 = list(data_jiaoyi_liuzhuan_count.iloc[:, 1])
    jiaoyi_liuzhuan_name2 = list(data_jiaoyi_liuzhuan_mj.iloc[:, 0])
    jiaoyi_liuzhuan_mj2 = list(data_jiaoyi_liuzhuan_mj.iloc[:, 2])

    if zs_mj=='zs':
        jiaoyi_liuzhuan_title1 = str(arrow.now().shift(days=days,months=-1).year) + '年' + str(
            arrow.now().shift(days=days,months=-1).month) + '月土流网交易土地流转类型宗数占比'
        jiaoyi_liuzhuan_pie1 = Pie(jiaoyi_liuzhuan_title1, title_pos='center', width=width, height=height)
        jiaoyi_liuzhuan_pie1.add("", jiaoyi_liuzhuan_name1, jiaoyi_liuzhuan_count1, radius=[25, 50],
                                 label_text_color=None,
                                 is_label_show=True, is_legend_show=False, legend_orient='vertical',
                                 legend_pos='left')
        jiaoyi_liuzhuan_pie1.render()
        return jiaoyi_liuzhuan_pie1

    elif zs_mj=='mj':
        jiaoyi_liuzhuan_title2 = str(arrow.now().shift(days=days,months=-1).year) + '年' + str(
            arrow.now().shift(days=days,months=-1).month) + '月土流网交易土地流转类型面积占比'
        jiaoyi_liuzhuan_pie2 = Pie(jiaoyi_liuzhuan_title2, title_pos='center', width=width, height=height)
        jiaoyi_liuzhuan_pie2.add("", jiaoyi_liuzhuan_name2, jiaoyi_liuzhuan_mj2, radius=[25, 50], label_text_color=None,
                                 is_label_show=True, is_legend_show=False, legend_orient='vertical',
                                 legend_pos='left')
        jiaoyi_liuzhuan_pie2.render()
        return jiaoyi_liuzhuan_pie2


def jiaoyi_size(conn,days,width,height):
    sql_jiaoyi_size = "select dikuai,count,mj from kanban_jiaoyi_dikuai where create_date= (select max(create_date) from kanban_jiaoyi_dikuai)"
    data_jiaoyi_size = pd.read_sql(sql_jiaoyi_size, conn)

    jiaoyi_size_title = str(arrow.now().shift(days=days,months=-1).year) + '年' + str(
        arrow.now().shift(days=days,months=-1).month) + '月土流网各规模农业用地交易量（宗）'
    jiaoyi_size_type = list(data_jiaoyi_size.iloc[:, 0])
    jiaoyi_size_count = list(data_jiaoyi_size.iloc[:, 2])

    jiaoyi_size_bar = Bar(jiaoyi_size_title, title_pos='center', width=width, height=height)
    jiaoyi_size_bar.add("", jiaoyi_size_type, jiaoyi_size_count, is_stack=True)
    jiaoyi_size_bar.render()
    return jiaoyi_size_bar


def jiaoyi_nianxian(conn,days,width,height):
    sql_jiaoyi_nianxian = "select type,year from kanban_jiaoyi_nianxian where create_date= (select max(create_date) from kanban_jiaoyi_nianxian)"
    data_jiaoyi_nianxian = pd.read_sql(sql_jiaoyi_nianxian, conn)

    jiaoyi_nianxian_type = list(data_jiaoyi_nianxian.iloc[:, 0])
    jiaoyi_nianxian_year = list(data_jiaoyi_nianxian.iloc[:, 1])
    jiaoyi_nianxian_title = str(arrow.now().shift(days=days,months=-1).year) + '年' + str(
        arrow.now().shift(days=days,months=-1).month) + '月土流网交易土地各土地类型平均流转年限'
    jiaoyi_nianxian_bar = Bar(jiaoyi_nianxian_title, title_pos='center', width=width, height=height)
    jiaoyi_nianxian_bar.add("", jiaoyi_nianxian_type, jiaoyi_nianxian_year, is_stack=True, xaxis_interval=0)
    jiaoyi_nianxian_bar.render()
    return jiaoyi_nianxian_bar


def jiaoyi_haoshi(conn,days,width,height):
    sql_jiaoyi_haoshi = "select type,time from kanban_jiaoyi_haoshi where create_date= (select max(create_date) from kanban_jiaoyi_haoshi)"
    data_jiaoyi_haoshi = pd.read_sql(sql_jiaoyi_haoshi, conn)

    jiaoyi_haoshi_type = list(data_jiaoyi_haoshi.iloc[:, 0])
    jiaoyi_haoshi_time = list(data_jiaoyi_haoshi.iloc[:, 1])
    jiaoyi_haoshi_title = str(arrow.now().shift(days=days,months=-1).year) + '年' + str(
        arrow.now().shift(days=days,months=-1).month) + '月土流网成交土地平均耗时（天）'
    jiaoyi_haoshi_bar = Bar(jiaoyi_haoshi_title, title_pos='center', width=width, height=height)
    jiaoyi_haoshi_bar.add("", jiaoyi_haoshi_type, jiaoyi_haoshi_time, is_stack=True, xaxis_interval=0)
    jiaoyi_haoshi_bar.render()
    return jiaoyi_haoshi_bar




def xuqiu_map(conn,width,height):
    sql_xuqiu_map = "select name,count,mj from kanban_xuqiu_map where create_date= (select max(create_date) from kanban_xuqiu_map)"
    data_xuqiu_map = pd.read_sql(sql_xuqiu_map, conn)

    fabu_xuqiu_name = list(data_xuqiu_map.iloc[:, 0])
    fabu_xuqiu_count = list(data_xuqiu_map.iloc[:, 1])

    fabu_xuqiu_map = Map("土流网最近1年土地需求发布数区域分布热力图（单位：宗）", width=width, height=height)
    fabu_xuqiu_map.add("", fabu_xuqiu_name, fabu_xuqiu_count, maptype="china", is_visualmap=True,
                       visual_range=[0, data_xuqiu_map.iloc[0, 1]],
                       visual_range_color=['#FAF0E6', '#FE9A2E', '#FE642E'], is_label_show=True)
    fabu_xuqiu_map.render()
    return fabu_xuqiu_map

def xuqiu_diqu(conn,days,width,height):
    sql_xuqiu_diqu = "select name,count,mj from kanban_xuqiu_diqu where create_date= (select max(create_date) from kanban_xuqiu_diqu)"
    data_xuqiu_diqu = pd.read_sql(sql_xuqiu_diqu, conn)

    xuqiu_diqu_name = list(data_xuqiu_diqu.iloc[:, 0])
    xuqiu_diqu_mj = list(data_xuqiu_diqu.iloc[:, 2])
    xuqiu_diqu_count = list(data_xuqiu_diqu.iloc[:, 1])

    xuqiu_diqu_title = str(arrow.now().shift(days=days,months=-1).year) + '年' + str(
        arrow.now().shift(days=days,months=-1).month) + '月土流网土地需求区域分布'
    xuqiu_diqu_bar = Bar(xuqiu_diqu_title)
    xuqiu_diqu_bar.add("面积（亩）", xuqiu_diqu_name, xuqiu_diqu_mj, xaxis_interval=0, xaxis_rotate=90)
    xuqiu_diqu_line = Line()
    xuqiu_diqu_line.add("宗数", xuqiu_diqu_name, xuqiu_diqu_count, xaxis_interval=0, xaxis_rotate=90)

    xuqiu_diqu_overlap = Overlap(height=height, width=width)
    xuqiu_diqu_overlap.add(xuqiu_diqu_bar)
    xuqiu_diqu_overlap.add(xuqiu_diqu_line, yaxis_index=1, is_add_yaxis=True)
    xuqiu_diqu_overlap.render()

    return xuqiu_diqu_overlap

def xuqiu_type(conn,days,width,height,zs_mj):
    sql_xuqiu_type = "select type,count,mj from kanban_xuqiu_type where create_date= (select max(create_date) from kanban_xuqiu_type)"
    data_xuqiu_type = pd.read_sql(sql_xuqiu_type, conn)

    date_xuqiu_type_count = data_xuqiu_type.sort_values('count', ascending=False)
    date_xuqiu_type_mj = data_xuqiu_type.sort_values('mj', ascending=False)

    xuqiu_type_name1 = list(date_xuqiu_type_count.iloc[:, 0])
    xuqiu_type_count1 = list(date_xuqiu_type_count.iloc[:, 1])
    xuqiu_type_name2 = list(date_xuqiu_type_mj.iloc[:, 0])
    xuqiu_type_mj2 = list(date_xuqiu_type_mj.iloc[:, 2])

    if zs_mj=='zs':
        xuqiu_type_title1 = str(arrow.now().shift(days=days,months=-1).year) + '年' + str(
            arrow.now().shift(days=days,months=-1).month) + '月土流网土地需求类型宗数占比'
        xuqiu_type_pie1 = Pie(xuqiu_type_title1, title_pos='center', width=width, height=height)
        xuqiu_type_pie1.add("", xuqiu_type_name1, xuqiu_type_count1, rosetype='radius', radius=[25, 50],
                            label_text_color=None,
                            is_label_show=True, is_legend_show=False, legend_orient='vertical',
                            legend_pos='left')
        xuqiu_type_pie1.render()
        return xuqiu_type_pie1

    if zs_mj == 'mj':
        xuqiu_type_title2 = str(arrow.now().shift(days=days,months=-1).year) + '年' + str(
            arrow.now().shift(days=days,months=-1).month) + '月土流网土地需求类型面积占比'
        xuqiu_type_pie2 = Pie(xuqiu_type_title2, title_pos='center', width=width, height=height)
        xuqiu_type_pie2.add("", xuqiu_type_name2, xuqiu_type_mj2, rosetype='radius', radius=[25, 50],
                            label_text_color=None,
                            is_label_show=True, is_legend_show=False, legend_orient='vertical',
                            legend_pos='left')
        xuqiu_type_pie2.render()
        return xuqiu_type_pie2