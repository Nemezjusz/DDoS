from flask import Flask, render_template
import time
app = Flask(__name__)

def do_someting():
    x = 150*32
    x = x^23

    return time.time()

@app.route('/', methods=['POST', 'GET'])
def index():

    tx = do_someting()

    return render_template("main2.html", text = tx)


