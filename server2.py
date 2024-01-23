import os.path
from flask import Flask, render_template, request
import datetime

app = Flask(__name__)
def do_someting():
    x = 150*32
    x = x^44

    return datetime.datetime.now()
@app.route('/', methods=['POST', 'GET'])
def index():
    login = request.form.get('login')
    do_someting()

    if login is None:
        return render_template("time.html")
    else:
        return render_template("welcome.html", login=login)




