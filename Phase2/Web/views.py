from flask import Flask, render_template

from udeltio import app, db
# from api.v1_0.views import *

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
	return render_template('index.html')