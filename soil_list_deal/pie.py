from flask import Flask, render_template

app = Flask(__name__)

@app.route("/pie/",methods=['GET','POST'])
def pie():

    return render_template("pie.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=328,
            debug=True)