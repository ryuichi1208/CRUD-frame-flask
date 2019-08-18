#! /usr/bin/env python

import os
import numpy as np

from flask import (
    Flask, request, jsonify, render_template, redirect,
    url_for, abort
)
from src import *

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/300', methods=['GET'])
def eroor_redirect():
    abort(400)


@app.errorhandler(400)
def error_handler(error):
    return render_template("300.html"), error.code


@app.errorhandler(404)
def error_handler(error):
    return render_template("404.html"), error.code


@app.route('/api/v1/book', methods=['GET'])
def read():
    path = request.args.get("path") or "data/sample.json"
    js = rb.read_book_info(path)
    return jsonify(js)


if __name__ == '__main__':
    CRUD_JSON_AS_ASCII = os.getenv('JSON_AS_ASCII') or False
    CRUD_FLASK_DEBUG_MODE = os.getenv('FLASK_DEBUG_MODE') or True
    CRUD_FLASK_IP_ADDR = os.getenv('FLASK_IP_ADDR') or "0.0.0.0"
    CRUD_FLASK_PORT = os.getenv('FLASK_PORE_NUM') or 5000

    app.config['JSON_AS_ASCII'] = CRUD_JSON_AS_ASCII
    app.debug = CRUD_FLASK_DEBUG_MODE
    app.run(host=CRUD_FLASK_IP_ADDR, port=CRUD_FLASK_PORT)
