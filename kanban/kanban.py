from flask import Flask, render_template
from kanban_tu import *
from kanban_tu_mon import *
import arrow
import pymysql

app = Flask(__name__)
REMOTE_HOST = "/static/js"



@app.route("/tlw/kanban/")
def kanban():
    dbconn = pymysql.connect(
        host="10.10.66.8",
        database="seo_cai",
        user="caizhiwei",
        password="20180803",
        port=3306,
        charset='utf8'
    )
    #days是为了与kettle定时任务同步，每月更新数据后，更新图表标题日期
    days=-3

    #pyecharts生成图表
    fabu_diqu_a = fabu_diqu(dbconn,days,820, 400)
    fabu_map_a = fabu_map(dbconn,820, 820)
    fabu_type1_a = fabu_type(dbconn,days,400, 400, 'zs')
    fabu_type2_a = fabu_type(dbconn,days,400, 400, 'mj')
    fabu_liuzhuan1_a = fabu_liuzhuan(dbconn,days,400, 400, 'zs')
    fabu_liuzhuan2_a = fabu_liuzhuan(dbconn,days,400, 400, 'mj')
    fabu_size_a = fabu_size(dbconn,days,820, 400)
    fabu_nianxian_a = fabu_nianxian(dbconn,days,820, 400)
    fabu_label_a = fabu_label(dbconn,days,820, 400)

    xuqiu_diqu_a = xuqiu_diqu(dbconn,days,820, 400)
    xuqiu_map_a = xuqiu_map(dbconn,820, 820)
    xuqiu_type1_a = xuqiu_type(dbconn,days,400, 400, 'zs')
    xuqiu_type2_a = xuqiu_type(dbconn,days,400, 400, 'mj')

    jiaoyi_diqu_a = jiaoyi_diqu(dbconn,days,820, 400)
    jiaoyi_map_a = jiaoyi_map(dbconn,820, 820)
    jiaoyi_type1_a = jiaoyi_type(dbconn,days,400, 400, 'zs')
    jiaoyi_type2_a = jiaoyi_type(dbconn,days,400, 400, 'mj')
    jiaoyi_liuzhuan1_a = jiaoyi_liuzhuan(dbconn,days,400, 400, 'zs')
    jiaoyi_liuzhuan2_a = jiaoyi_liuzhuan(dbconn,days,400, 400, 'mj')
    jiaoyi_size_a = jiaoyi_size(dbconn,days,820, 400)
    jiaoyi_nianxian_a = jiaoyi_nianxian(dbconn,days,820, 400)
    jiaoyi_haoshi_a = jiaoyi_haoshi(dbconn,days,820, 400)

    dbconn.close()

    #渲染图表
    return render_template(
        "kanban.html",
        biaoti=str(arrow.now().shift(days=-3,months=-1).year) + '年' +
        str(arrow.now().shift(days=-3,months=-1).month) + '月份土地流转市场土地发布及交易数据',
        host=REMOTE_HOST,

        script_list1=fabu_map_a.get_js_dependencies(),
        script_list2=fabu_label_a.get_js_dependencies(),
        myechart1=fabu_diqu_a.render_embed(),
        myechart2=fabu_map_a.render_embed(),
        myechart3=fabu_type1_a.render_embed(),
        myechart4=fabu_type2_a.render_embed(),
        myechart5=fabu_liuzhuan1_a.render_embed(),
        myechart6=fabu_liuzhuan2_a.render_embed(),
        myechart7=fabu_size_a.render_embed(),
        myechart8=fabu_nianxian_a.render_embed(),
        myechart9=fabu_label_a.render_embed(),

        script_list001=xuqiu_map_a.get_js_dependencies(),
        myechart002=xuqiu_diqu_a.render_embed(),
        myechart001=xuqiu_map_a.render_embed(),
        myechart003=xuqiu_type1_a.render_embed(),
        myechart004=xuqiu_type2_a.render_embed(),

        script_list01=jiaoyi_map_a.get_js_dependencies(),
        myechart01=jiaoyi_diqu_a.render_embed(),
        myechart02=jiaoyi_map_a.render_embed(),
        myechart03=jiaoyi_type1_a.render_embed(),
        myechart04=jiaoyi_type2_a.render_embed(),
        myechart05=jiaoyi_liuzhuan1_a.render_embed(),
        myechart06=jiaoyi_liuzhuan2_a.render_embed(),
        myechart07=jiaoyi_size_a.render_embed(),
        myechart08=jiaoyi_nianxian_a.render_embed(),
        myechart09=jiaoyi_haoshi_a.render_embed(),
    )


@app.route("/tlw/kanban/<mon>/")
def kanban_mon(mon):
    dbconn = pymysql.connect(
        host="10.10.66.8",
        database="seo_cai",
        user="caizhiwei",
        password="20180803",
        port=3306,
        charset='utf8'
    )

    # pyecharts生成图表
    fabu_diqu_a_mon = fabu_diqu_mon(dbconn,820, 400,mon)
    fabu_map_a = fabu_map_mon(dbconn,820, 820,mon)
    fabu_type1_a = fabu_type_mon(dbconn,400, 400, 'zs',mon)
    fabu_type2_a = fabu_type_mon(dbconn,400, 400, 'mj',mon)
    fabu_liuzhuan1_a = fabu_liuzhuan_mon(dbconn,400, 400, 'zs',mon)
    fabu_liuzhuan2_a = fabu_liuzhuan_mon(dbconn,400, 400, 'mj',mon)
    fabu_size_a = fabu_size_mon(dbconn,820, 400,mon)
    fabu_nianxian_a = fabu_nianxian_mon(dbconn,820, 400,mon)
    fabu_label_a = fabu_label_mon(dbconn,820, 400,mon)

    xuqiu_diqu_a = xuqiu_diqu_mon(dbconn,820, 400,mon)
    xuqiu_map_a = xuqiu_map_mon(dbconn,820, 820,mon)
    xuqiu_type1_a = xuqiu_type_mon(dbconn,400, 400, 'zs',mon)
    xuqiu_type2_a = xuqiu_type_mon(dbconn,400, 400, 'mj',mon)

    jiaoyi_diqu_a = jiaoyi_diqu_mon(dbconn,820, 400,mon)
    jiaoyi_map_a = jiaoyi_map_mon(dbconn,820, 820,mon)
    jiaoyi_type1_a = jiaoyi_type_mon(dbconn,400, 400, 'zs',mon)
    jiaoyi_type2_a = jiaoyi_type_mon(dbconn,400, 400, 'mj',mon)
    jiaoyi_liuzhuan1_a = jiaoyi_liuzhuan_mon(dbconn,400, 400, 'zs',mon)
    jiaoyi_liuzhuan2_a = jiaoyi_liuzhuan_mon(dbconn,400, 400, 'mj',mon)
    jiaoyi_size_a = jiaoyi_size_mon(dbconn,820, 400,mon)
    jiaoyi_nianxian_a = jiaoyi_nianxian_mon(dbconn,820, 400,mon)
    jiaoyi_haoshi_a = jiaoyi_haoshi_mon(dbconn,820, 400,mon)

    dbconn.close()

    # 渲染图表
    return render_template(
        "kanban.html",
        biaoti=str(mon)[:4] + '年' + str(mon)[-2:] + '月份土地流转市场土地发布及交易数据',
        host=REMOTE_HOST,

        script_list1=fabu_map_a.get_js_dependencies(),
        script_list2=fabu_label_a.get_js_dependencies(),
        myechart1=fabu_diqu_a_mon.render_embed(),
        myechart2=fabu_map_a.render_embed(),
        myechart3=fabu_type1_a.render_embed(),
        myechart4=fabu_type2_a.render_embed(),
        myechart5=fabu_liuzhuan1_a.render_embed(),
        myechart6=fabu_liuzhuan2_a.render_embed(),
        myechart7=fabu_size_a.render_embed(),
        myechart8=fabu_nianxian_a.render_embed(),
        myechart9=fabu_label_a.render_embed(),

        script_list001=xuqiu_map_a.get_js_dependencies(),
        myechart002=xuqiu_diqu_a.render_embed(),
        myechart001=xuqiu_map_a.render_embed(),
        myechart003=xuqiu_type1_a.render_embed(),
        myechart004=xuqiu_type2_a.render_embed(),

        script_list01=jiaoyi_map_a.get_js_dependencies(),
        myechart01=jiaoyi_diqu_a.render_embed(),
        myechart02=jiaoyi_map_a.render_embed(),
        myechart03=jiaoyi_type1_a.render_embed(),
        myechart04=jiaoyi_type2_a.render_embed(),
        myechart05=jiaoyi_liuzhuan1_a.render_embed(),
        myechart06=jiaoyi_liuzhuan2_a.render_embed(),
        myechart07=jiaoyi_size_a.render_embed(),
        myechart08=jiaoyi_nianxian_a.render_embed(),
        myechart09=jiaoyi_haoshi_a.render_embed(),
    )




if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=1213,
            debug=True)

