from flask import Flask
from flask import request

from random import randint

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return f"Hello world!{randint(0, 10)}"
