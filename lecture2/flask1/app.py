from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return dict(request.headers)
