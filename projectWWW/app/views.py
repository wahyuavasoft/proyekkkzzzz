from flask import render_template
from app import app
import json,urllib, sys


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': '</python>'}
    return render_template('index.html',title='project',user=user)





