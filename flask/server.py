#!/usr/bin/env python3

from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def index():
    return '''<!doctype html>
    <html>
        <body>
            <h1><a href="/">show</a</h1>
            <ol>
                <li><a href="/read/1/">bdm</a></li>
                <li><a href="/read/2/">lcp</a></li>
                <li><a href="/read/3/">pip</a></li>
            </ol>
            <h2>Welcome</h2>
            Hello, Web
        </body>
    </html>
    '''


@app.route('/create/')
def create():
    return 'create'

app.run(host='0.0.0.0', port=9900, debug=True)