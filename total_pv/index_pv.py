from flask import Flask, render_template,request
import pymysql
import arrow

app = Flask(__name__)


@app.route("/loc/",methods=['GET','POST'])


def loc():
    # 获取统计截止日期
    t_loc = arrow.now().shift(days=-1)
    jiezhi_date_loc = '——统计数据截至日期：' + str(t_loc.year) + '年' + str(t_loc.month) + '月' \
                  + str(t_loc.day) + '日'
    #数据库连接
    dbconn = pymysql.connect(
        host="******",
        user="******",
        password="******",
        port=3306,
        charset='utf8',
        db='******')

    #读取sql获取省、市pv数据
    sql_province = '''
    SELECT province,sum(pv) from sv_loc_pv
    GROUP BY province_id
    ORDER BY sum(pv) desc
    '''

    sql_city = '''
    SELECT province,city,sum(pv) from sv_loc_pv
    GROUP BY province_id,city_id
    ORDER BY province_id,sum(pv) desc,city_id
    '''
    cursor_province = dbconn.cursor()
    cursor_city = dbconn.cursor()

    cursor_province.execute(sql_province)
    cursor_city.execute(sql_city)

    data_province = cursor_province.fetchall()
    data_city = cursor_city.fetchall()

    dbconn.commit()
    cursor_province.close()
    cursor_city.close()
    dbconn.close()

    #将数据转化为省、市对应的字典格式
    series = {}
    for row in data_city:
        if series.get(row[0]) is None:
            series[row[0]] = []
        series[row[0]].append([row[1], row[2]])
    #将decimal数据格式转化为int格式
    for value in series.values():
        for ls in value:
            ls[1] = int(ls[1])



    return render_template("loc.html",data_province=data_province,
                           series=series,jiezhi_date = jiezhi_date_loc)

@app.route("/type/",methods=['GET','POST'])

def type():
    #获取统计截止日期
    t_type = arrow.now().shift(days=-1)
    jiezhi_date_type = '——统计数据截至日期：' + str(t_type.year) + '年' + str(t_type.month) + '月' \
                  + str(t_type.day) + '日'

    #数据库连接
    dbconn_diqu = pymysql.connect(
        host="***",
        user="***",
        password="***",
        port=3306,
        charset='utf8',
        db='***')

    #读取sql获取省市信息数据
    sql_diqu = 'SELECT province,city from sv_loctype_pv group by province_id ,city_id ORDER BY province_id ,city_id'

    cur_diqu = dbconn_diqu.cursor()
    cur_diqu.execute(sql_diqu)
    data_diqu = cur_diqu.fetchall()
    dbconn_diqu.commit()
    cur_diqu.close()
    dbconn_diqu.close()

    #数据转化为省、市对应字典格式
    series_diqu = {}
    for row_diqu in data_diqu:
        if series_diqu.get(row_diqu[0]) is None:
            series_diqu[row_diqu[0]] = []
        series_diqu[row_diqu[0]].append((row_diqu[1]))

    #数据转化为省、市列表格式，用于传入模板
    arr_province = ['请选择省/城市']
    arr_city = [['请选择城市/地区']]
    for (key_diqu, value_diqu) in series_diqu.items():
        arr_province.append(key_diqu)
        arr_city.append(value_diqu)
    #获取省、市表单控件数据
    diqu_pro = request.form.get("province")
    diqu_ct = request.form.get("city")

    #数据库连接
    dbconn_type = pymysql.connect(
        host="******",
        user="******",
        password="*****",
        port=3306,
        charset='utf8',
        db='*******')

    #读取sql获取各土地类型pv数据
    if diqu_ct and diqu_ct != '请选择城市/地区':

        sql_type_province = '''SELECT province,city,type2, sum(pv) as sum_pv from sv_loctype_pv 
        where province = '%s' and city = '%s' GROUP BY province_id,city_id,type2 
        ORDER BY sum_pv desc'''%(diqu_pro,diqu_ct)

        sql_type_city = '''SELECT province,city,type2,type1 ,sum(pv) as sum_pv from sv_loctype_pv 
        where province = '%s'and city ='%s' GROUP BY province_id,city_id,type2,type1 
        ORDER BY province_id,city_id,sum_pv desc'''%(diqu_pro,diqu_ct)

        choose_pro_city='\''+str(diqu_pro)+'-'+str(diqu_ct) +'-服务中心土地详情页累计PV\''

    else:
        sql_type_province = 'SELECT province,city,type2, sum(pv) as sum_pv from sv_loctype_pv ' + \
                            ' GROUP BY type2 ORDER BY sum_pv desc'

        sql_type_city = 'SELECT province,city,type2,type1 ,sum(pv) as sum_pv from sv_loctype_pv ' + \
                        ' GROUP BY type2,type1 ORDER BY sum_pv desc'

        choose_pro_city='\'全国-服务中心土地详情页累计PV\''



    cur_type_province = dbconn_type.cursor()
    cur_type_city = dbconn_type.cursor()

    cur_type_province.execute(sql_type_province)
    cur_type_city.execute(sql_type_city)

    data_type_province = cur_type_province.fetchall()
    data_type_city = cur_type_city.fetchall()

    dbconn_type.commit()
    cur_type_province.close()
    cur_type_city.close()
    dbconn_type.close()


    #将省份土地类型pv数据转化为列表格式,用于柱图一级数据
    data_province_pic=[]
    for row_pic2 in data_type_province:
        data_province_pic.append(list(row_pic2))
    #将数据decimal转化为int格式
    for row_pic3 in data_province_pic:
        row_pic3[3]=int(row_pic3[3])

    #将省市数据转化为土地一级分类、二级分类对应的字典格式，用于柱图二级数据
    series_pic = {}
    for row_pic in data_type_city:
        if series_pic.get(row_pic[2]) is None:
            series_pic[row_pic[2]] = []
        series_pic[row_pic[2]].append([row_pic[3], row_pic[4]])
    #将decimal数据格式转化为int格式
    for value in series_pic.values():
        for ls in value:
            ls[1] = int(ls[1])


    return render_template("type.html",data_province_pic=data_province_pic,choose_pro_city=choose_pro_city,
                           series_pic=series_pic,arr_pro=arr_province,arr_city=arr_city,jiezhi_date2 = jiezhi_date_type)

@app.route("/user/",methods=['GET','POST'])

def user():


    #数据库连接
    dbconn_sv = pymysql.connect(
        host="10.10.66.8",
        user="caizhiwei",
        password="20180803",
        port=3306,
        charset='utf8',
        db='seo_cai')

    #读取sql获取省市信息数据
    sql_sv = 'SELECT province,sv_name from sv_loc_user_act group by province_id ,sv_id ORDER BY province_id ,sv_id'

    cur_sv = dbconn_sv.cursor()
    cur_sv.execute(sql_sv)
    data_sv = cur_sv.fetchall()
    dbconn_sv.commit()
    cur_sv.close()
    dbconn_sv.close()

    #数据转化为省、服务中心对应字典格式
    series_sv = {}
    for row_sv in data_sv:
        if series_sv.get(row_sv[0]) is None:
            series_sv[row_sv[0]] = []
        series_sv[row_sv[0]].append((row_sv[1]))

    #数据转化为省、市列表格式，用于传入模板
    arr_province_sv = ['请选择省/城市']
    arr_sv = [['请选择服务中心']]
    for (key_sv, value_sv) in series_sv.items():
        arr_province_sv.append(key_sv)
        arr_sv.append(value_sv)
    #获取省、服务中心表单控件数据
    get_pro = request.form.get("get_pro")
    get_sv = request.form.get("get_sv")

    #数据库连接
    dbconn_date = pymysql.connect(
        host="***",
        user="***",
        password="***",
        port=3306,
        charset='utf8',
        db='***')

    #读取sql获取各类型各时间用户行为数据
    if get_pro and get_sv != '请选择服务中心':

        sql_user_type = '''SELECT province,sv_name,type, sum(count) as sum_count from sv_loc_user_act 
        where province = '%s' and sv_name = '%s' GROUP BY province_id,sv_id,type
        ORDER BY FIELD(`type`,'查看电话号码','点击拨打电话','点击环信IM')'''%(get_pro,get_sv)

        sql_type_sv = '''SELECT province,sv_name,type,date ,sum(count) as sum_count from sv_loc_user_act 
        where province = '%s'and sv_name ='%s' GROUP BY province_id,sv_id,type,date
        ORDER BY province_id,sv_id,date '''%(get_pro,get_sv)

        choose_pro_sv='\''+str(get_sv) +'-土地详情页用户行为数据\''

    else:
        sql_user_type = '''SELECT province,sv_name,type, sum(count) as sum_count from sv_loc_user_act
        GROUP BY type ORDER BY FIELD(`type`,'查看电话号码','点击拨打电话','点击环信IM')'''

        sql_type_sv = '''SELECT province,sv_name,type,date ,sum(count) as sum_count from sv_loc_user_act  
        GROUP BY type,date ORDER BY date'''

        choose_pro_sv='\'全国-服务中心土地详情页用户行为数据\''



    cur_user_type = dbconn_date.cursor()
    cur_type_sv = dbconn_date.cursor()

    cur_user_type.execute(sql_user_type)
    cur_type_sv.execute(sql_type_sv)

    data_user_type = cur_user_type.fetchall()
    data_type_sv = cur_type_sv.fetchall()

    dbconn_date.commit()
    cur_user_type.close()
    cur_type_sv.close()
    dbconn_date.close()


    #将省份用户行为数据转化为列表格式,用于柱图一级数据
    data_user_pic=[]
    for row_pic4 in data_user_type:
        data_user_pic.append(list(row_pic4))
    #将decimal数据转化为int格式
    for row_pic5 in data_user_pic:
        row_pic5[3]=int(row_pic5[3])

    #将省市数据转化为用户行为、时间对应的字典格式，用于柱图二级数据
    series_user = {}
    for row_pic6 in data_type_sv:
        if series_user.get(row_pic6[2]) is None:
            series_user[row_pic6[2]] = []
        series_user[row_pic6[2]].append([row_pic6[3], row_pic6[4]])
    #将decimal数据格式转化为int格式
    for value2 in series_user.values():
        for ls2 in value2:
            ls2[0]=ls2[0].strftime("%Y-%m-%d")
            ls2[1] = int(ls2[1])


    return render_template("user.html",data_user_pic=data_user_pic,choose_pro_sv=choose_pro_sv,
                           series_user=series_user,arr_province_sv=arr_province_sv,arr_sv=arr_sv)


if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=1225,
            debug=True)
