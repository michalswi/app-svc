from flask import Flask, request
from flask import Response

import requests

from checkStatus import get_status_code


app = Flask(__name__)

URL = "http://localhost:8000"

@app.route('/', methods=['GET'])
def home():
    return "hello world\n"

@app.route('/hz', methods=['GET'])
def gethz():
    return "OK", 200

@app.route('/healthz', methods=['GET'])
def get():
    """health check"""
    
    # NO verification
    # return "OK", 200

    # WITH verification
    if get_status_code(URL) == 200:
        return Response("ok", status = 200)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = False)