# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from naming import parse_name


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    name = request.args.get('name')
    status = []
    if name:
        status = parse_name(name.encode('utf-8').encode('base64'))
    return render_template('index.html', status=status)
