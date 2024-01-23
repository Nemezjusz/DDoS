from flask import Flask, render_template
import datetime
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)


def do_someting():
    x = 150*32
    x = x^44

    return datetime.datetime.now()

@app.route('/', methods=['POST', 'GET'])
def index():

    tx = do_someting()

    return render_template("signin.html", text = tx)


