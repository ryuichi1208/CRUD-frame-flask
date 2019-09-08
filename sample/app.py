from flask import Flask
import os
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    pid = os.getpid()
    now = datetime.datetime.now().strftime('%H:%M:%S.%f')
    return f'<h1>Welcom!({now}) pid:{pid}</h1>\n'

@app.route('/sample')
def sample():
    now = datetime.datetime.now().strftime('%H:%M:%S.%f')
    return f'<h1>sample page!({now})</h1>\n'
