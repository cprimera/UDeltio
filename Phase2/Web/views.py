from flask import Flask, render_template

from udeltio import app, db
<<<<<<< HEAD
# from api.v1_0.views import *
=======
from api.v1_0.views import *
from oauth2.views import *
>>>>>>> master

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
	return render_template('index.html')