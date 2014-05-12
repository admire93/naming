# -*- coding: utf-8 -*-
from time import ctime

from flask import Flask, render_template, request
from naming import parse_name


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    name = request.args.get('name')
    status = []
    if name:
        n = name.encode('utf-8')
        r = (n + ctime()).encode('base64')
        status = parse_name(n)
    return render_template('index.html', status=status)
