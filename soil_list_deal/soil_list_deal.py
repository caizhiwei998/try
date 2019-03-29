from flask import Flask, render_template
import pymysql
import arrow

app = Flask(__name__)


@app.route("/soil_list/num/",methods=['GET','POST'])
def soil_list_num():
    # 获取统计截止日期
    t_loc = arrow.now().shift(days=-1)
    jiezhi_date = '——统计数据截至日期：' + str(t_loc.year) + '年' + str(t_loc.month) + '月' \
                  + str(t_loc.day) + '日'
    #数据库连接
    dbconn = pymysql.connect(
        host="******",
        user="******",
        password="******",
        port=3306,
        charset='utf8',
        db='******')

    sql_province = '''
    SELECT province,sum(num) as num from    
    drill_soil_list
    group by province
    order by num desc
    '''

    sql_city = '''
    SELECT province,city,sum(num) as num from
    drill_soil_list
    group by province,city
    order by num desc
    '''

    sql_county = '''
    SELECT province,city,county,num from
    drill_soil_list
    order by num desc
    '''
    cur = dbconn.cursor()
    cur.execute(sql_province)
    data_province = cur.fetchall()

    cur.execute(sql_city)
    data_city = cur.fetchall()

    cur.execute(sql_county)
    data_county = cur.fetchall()
    cur.close()
    dbconn.close()


    #将city数据转为列表格式
    ls_city = []
    for row in data_city:
        ls_city.append([row[0], row[1], int(row[2])]) #[province,city,num]

    #city数据第一次遍历 传入省份字典数据
    name1 = []
    result = []
    for row in ls_city:
        if row[0] not in name1 and row[0] != None:
            name1.append(row[0])
            result.append({'name': row[0], 'id': row[0], 'data': [],'colorByPoint': 'true'})

    #city数据第二次遍历 传入市区字典数据（包括数值）
    name2 = []
    for row in ls_city:
        if row[1] not in name2 and row[1] != None:
            name2.append(row[1])
            d = {'name': row[1], 'y': row[2], 'drilldown': row[1],'colorByPoint': 'true'}
            for i in result:
                if i['name'] == row[0]:
                    i['data'].append(d)

    # 将county数据转为列表格式
    ls_county = []
    for row in data_county:
        ls_county.append([row[0], row[1], row[2],int(row[3])]) #[province,city,county,num]

    #county数据第一次遍历 传入市区字典数据
    name3 = []
    for row in ls_county:
        if row[1] not in name3 and row[1] != None:
            name3.append(row[1])
            result.append({'name': row[1], 'id': row[1], 'data': [],'colorByPoint': 'true'})

    #county数据第二次遍历 传入县区字典数据（包括数值）
    name4 = []
    for row in ls_county:
        if row[2] not in name4 and row[2] != None:
            name2.append(row[2])
            d = {'name': row[2], 'y': row[3], 'drilldown': row[1],'colorByPoint': 'true'}
            for i in result:
                if i['name'] == row[1]:
                    i['data'].append(d)

    series = str(result)
    series = series.replace("'name'", "name").replace("'id'", "id").replace("'drilldown'", "drilldown")\
        .replace("'y'","y").replace("'data'","data").replace("'colorByPoint'","colorByPoint")\
        .replace("'true'","true")

    return render_template("soil_list_num.html",series=series,
                           data_province=data_province,
                           jiezhi_date = jiezhi_date)


@app.route("/soil_list/area/",methods=['GET','POST'])
def soil_list_area():
    # 获取统计截止日期
    t_loc = arrow.now().shift(days=-1)
    jiezhi_date = '——统计数据截至日期：' + str(t_loc.year) + '年' + str(t_loc.month) + '月' \
                  + str(t_loc.day) + '日'
    #数据库连接
    dbconn = pymysql.connect(
        host="******",
        user="******",
        password="******",
        port=3306,
        charset='utf8',
        db='******')

    sql_province = '''
    SELECT province,sum(area) as area from    
    drill_soil_list
    group by province
    order by area desc
    '''

    sql_city = '''
    SELECT province,city,sum(area) as area from
    drill_soil_list
    group by province,city
    order by area desc
    '''

    sql_county = '''
    SELECT province,city,county,area from
    drill_soil_list
    order by area desc
    '''
    cur = dbconn.cursor()
    cur.execute(sql_province)
    data_province = cur.fetchall()

    cur.execute(sql_city)
    data_city = cur.fetchall()

    cur.execute(sql_county)
    data_county = cur.fetchall()
    cur.close()
    dbconn.close()


    #将city数据转为列表格式
    ls_city = []
    for row in data_city:
        ls_city.append([row[0], row[1], int(row[2])]) #[province,city,area]

    #city数据第一次遍历 传入省份字典数据
    name1 = []
    result = []
    for row in ls_city:
        if row[0] not in name1 and row[0] != None:
            name1.append(row[0])
            result.append({'name': row[0], 'id': row[0], 'data': [],'colorByPoint': 'true'})

    #city数据第二次遍历 传入市区字典数据（包括数值）
    name2 = []
    for row in ls_city:
        if row[1] not in name2 and row[1] != None:
            name2.append(row[1])
            d = {'name': row[1], 'y': row[2], 'drilldown': row[1],'colorByPoint': 'true'}
            for i in result:
                if i['name'] == row[0]:
                    i['data'].append(d)

    # 将county数据转为列表格式
    ls_county = []
    for row in data_county:
        ls_county.append([row[0], row[1], row[2],int(row[3])]) #[province,city,county,area]

    #county数据第一次遍历 传入市区字典数据
    name3 = []
    for row in ls_county:
        if row[1] not in name3 and row[1] != None:
            name3.append(row[1])
            result.append({'name': row[1], 'id': row[1], 'data': [],'colorByPoint': 'true'})

    #county数据第二次遍历 传入县区字典数据（包括数值）
    name4 = []
    for row in ls_county:
        if row[2] not in name4 and row[2] != None:
            name2.append(row[2])
            d = {'name': row[2], 'y': row[3], 'drilldown': row[1],'colorByPoint': 'true'}
            for i in result:
                if i['name'] == row[1]:
                    i['data'].append(d)

    series = str(result)
    series = series.replace("'name'", "name").replace("'id'", "id").replace("'drilldown'", "drilldown")\
        .replace("'y'","y").replace("'data'","data").replace("'colorByPoint'","colorByPoint")\
        .replace("'true'","true")

    return render_template("soil_list_area.html",series=series,
                           data_province=data_province,
                           jiezhi_date = jiezhi_date)


@app.route("/soil_deal/num/",methods=['GET','POST'])
def soil_deal_num():
    # 获取统计截止日期
    t_loc = arrow.now().shift(days=-1)
    jiezhi_date = '——统计数据截至日期：' + str(t_loc.year) + '年' + str(t_loc.month) + '月' \
                  + str(t_loc.day) + '日'
    #数据库连接
    dbconn = pymysql.connect(
        host="******",
        user="******",
        password="******",
        port=3306,
        charset='utf8',
        db='******')

    sql_province = '''
    SELECT province,sum(num) as num from    
    drill_soil_deal
    group by province
    order by num desc
    '''

    sql_city = '''
    SELECT province,city,sum(num) as num from
    drill_soil_deal
    group by province,city
    order by num desc
    '''

    sql_county = '''
    SELECT province,city,county,num from
    drill_soil_deal
    order by num desc
    '''
    cur = dbconn.cursor()
    cur.execute(sql_province)
    data_province = cur.fetchall()

    cur.execute(sql_city)
    data_city = cur.fetchall()

    cur.execute(sql_county)
    data_county = cur.fetchall()
    cur.close()
    dbconn.close()


    #将city数据转为列表格式
    ls_city = []
    for row in data_city:
        ls_city.append([row[0], row[1], int(row[2])]) #[province,city,num]

    #city数据第一次遍历 传入省份字典数据
    name1 = []
    result = []
    for row in ls_city:
        if row[0] not in name1 and row[0] != None:
            name1.append(row[0])
            result.append({'name': row[0], 'id': row[0], 'data': [],'colorByPoint': 'true'})

    #city数据第二次遍历 传入市区字典数据（包括数值）
    name2 = []
    for row in ls_city:
        if row[1] not in name2 and row[1] != None:
            name2.append(row[1])
            d = {'name': row[1], 'y': row[2], 'drilldown': row[1],'colorByPoint': 'true'}
            for i in result:
                if i['name'] == row[0]:
                    i['data'].append(d)

    # 将county数据转为列表格式
    ls_county = []
    for row in data_county:
        ls_county.append([row[0], row[1], row[2],int(row[3])]) #[province,city,county,num]

    #county数据第一次遍历 传入市区字典数据
    name3 = []
    for row in ls_county:
        if row[1] not in name3 and row[1] != None:
            name3.append(row[1])
            result.append({'name': row[1], 'id': row[1], 'data': [],'colorByPoint': 'true'})

    #county数据第二次遍历 传入县区字典数据（包括数值）
    name4 = []
    for row in ls_county:
        if row[2] not in name4 and row[2] != None:
            name2.append(row[2])
            d = {'name': row[2], 'y': row[3], 'drilldown': row[1],'colorByPoint': 'true'}
            for i in result:
                if i['name'] == row[1]:
                    i['data'].append(d)

    series = str(result)
    series = series.replace("'name'", "name").replace("'id'", "id").replace("'drilldown'", "drilldown")\
        .replace("'y'","y").replace("'data'","data").replace("'colorByPoint'","colorByPoint")\
        .replace("'true'","true")

    return render_template("soil_deal_num.html",series=series,
                           data_province=data_province,
                           jiezhi_date = jiezhi_date)


@app.route("/soil_deal/area/",methods=['GET','POST'])
def soil_deal_area():
    # 获取统计截止日期
    t_loc = arrow.now().shift(days=-1)
    jiezhi_date = '——统计数据截至日期：' + str(t_loc.year) + '年' + str(t_loc.month) + '月' \
                  + str(t_loc.day) + '日'
    #数据库连接
    dbconn = pymysql.connect(
        host="******",
        user="******",
        password="******",
        port=3306,
        charset='utf8',
        db='******')

    sql_province = '''
    SELECT province,sum(area) as area from    
    drill_soil_deal
    group by province
    order by area desc
    '''

    sql_city = '''
    SELECT province,city,sum(area) as area from
    drill_soil_deal
    group by province,city
    order by area desc
    '''

    sql_county = '''
    SELECT province,city,county,area from
    drill_soil_deal
    order by area desc
    '''
    cur = dbconn.cursor()
    cur.execute(sql_province)
    data_province = cur.fetchall()

    cur.execute(sql_city)
    data_city = cur.fetchall()

    cur.execute(sql_county)
    data_county = cur.fetchall()
    cur.close()
    dbconn.close()


    #将city数据转为列表格式
    ls_city = []
    for row in data_city:
        ls_city.append([row[0], row[1], int(row[2])]) #[province,city,area]

    #city数据第一次遍历 传入省份字典数据
    name1 = []
    result = []
    for row in ls_city:
        if row[0] not in name1 and row[0] != None:
            name1.append(row[0])
            result.append({'name': row[0], 'id': row[0], 'data': [],'colorByPoint': 'true'})

    #city数据第二次遍历 传入市区字典数据（包括数值）
    name2 = []
    for row in ls_city:
        if row[1] not in name2 and row[1] != None:
            name2.append(row[1])
            d = {'name': row[1], 'y': row[2], 'drilldown': row[1],'colorByPoint': 'true'}
            for i in result:
                if i['name'] == row[0]:
                    i['data'].append(d)

    # 将county数据转为列表格式
    ls_county = []
    for row in data_county:
        ls_county.append([row[0], row[1], row[2],int(row[3])]) #[province,city,county,area]

    #county数据第一次遍历 传入市区字典数据
    name3 = []
    for row in ls_county:
        if row[1] not in name3 and row[1] != None:
            name3.append(row[1])
            result.append({'name': row[1], 'id': row[1], 'data': [],'colorByPoint': 'true'})

    #county数据第二次遍历 传入县区字典数据（包括数值）
    name4 = []
    for row in ls_county:
        if row[2] not in name4 and row[2] != None:
            name2.append(row[2])
            d = {'name': row[2], 'y': row[3], 'drilldown': row[1],'colorByPoint': 'true'}
            for i in result:
                if i['name'] == row[1]:
                    i['data'].append(d)

    series = str(result)
    series = series.replace("'name'", "name").replace("'id'", "id").replace("'drilldown'", "drilldown")\
        .replace("'y'","y").replace("'data'","data").replace("'colorByPoint'","colorByPoint")\
        .replace("'true'","true")

    return render_template("soil_deal_area.html",series=series,
                           data_province=data_province,
                           jiezhi_date = jiezhi_date)

if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=8003,
            debug=True)
