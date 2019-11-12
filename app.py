from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def got_index():
    return render_template("index.html")

@app.route('/houses')
def got_houses():
    return render_template("house.html")

@app.route('/jon_snow')
def got_jon():
    return render_template("jon_snow.html")

@app.route('/daenerys_targaryen')
def got_danny():
    return render_template("daenerys_targaryen.html")