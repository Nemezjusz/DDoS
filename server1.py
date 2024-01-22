import os.path
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    login = request.form.get('login')
    if login is None:
        login = 'brak'


    return render_template("main.html")


