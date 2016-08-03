import os
from flask_login import LoginManager
from flask import Flask, request, redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from config import basedir

app = Flask(__name__, static_url_path='/static')
app.config.from_object('config')
app.jinja_env.autoescape = False
db=SQLAlchemy(app)

lm = LoginManager()
lm.init_app(app)


from app import views, models

