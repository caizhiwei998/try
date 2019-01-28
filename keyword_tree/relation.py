from flask import Flask, render_template
import pymysql
import json
from pyecharts import Tree
from pyecharts_javascripthon.api import TRANSLATOR

app = Flask(__name__)
REMOTE_HOST = "/static/js"

@app.route("/relation/",methods=['GET','POST'])

def relation():

    dbconn = pymysql.connect(
        host="10.10.66.8",
        user="caizhiwei",
        password="20180803",
        port=3306,
        charset="utf8",
        db="dqytlwork")

    #读取数据库JSON数据
    sql = "select json from words_relation_json where id =1"

    cursor = dbconn.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    dbconn.commit()
    cursor.close()
    dbconn.close()

    #字符串转JSON
    result = json.loads(data[0][0].replace("'", "\""))

    #树图
    tree = Tree(width=2000, height=2400)
    tree.add("", result, tree_collapse_interval=1)
    tree.render()
    javascript_snippet = TRANSLATOR.translate(tree.options)

    return render_template(
        "relation.html",
        chart_id=tree.chart_id,
        host=REMOTE_HOST,
        renderer=tree.renderer,
        my_width="95%",
        my_height=2400,
        custom_function=javascript_snippet.function_snippet,
        options=javascript_snippet.option_snippet,
        script_list=tree.get_js_dependencies(),

    )

if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=1222,
            debug=True)
