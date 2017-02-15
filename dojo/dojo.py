import os
from peewee import *
from super_sprinter_3000.connectdatabase import ConnectDatabase
from super_sprinter_3000.models import UserStories
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash, current_app


app = Flask(__name__)  # create the application instance :)
app.config.from_object(__name__)  # load config from this file , flaskr.py

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'dojo.db'),
    SECRET_KEY='development key'
))
app.config.from_envvar('DOJO_SETTINGS', silent=True)

@app.route('/')
def get_request():
    return render_template('')
    pass