#coding=utf-8

import os

from flask import Flask
from flask_mongoengine import MongoEngine
from flask_login import LoginManager
from flask_principal import Principal
from flask_moment import Moment

from.config import config

db = MongoEngine()

login_manager = LoginManager()
login_manager.session_protection = 'basic'
login_manager.login_view = 'accounts.login'

principals = Principal()

moment = Moment()


def create_app(config_name):
    app = Flask(__name__, template_folder=[config_name].TEMPLATE_PATH, static_folder=config[config_name].STATIC_PATH)
    app.config.from_object(config[config_name])

    db.init_app(app)
    login_manager.init_app(app)
    principals.init_app(app)
    moment.init_app(app)


    from main.urls import main as main_blueprint, blog_admin as blog_admin_blueprint
    from acc