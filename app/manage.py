#!user/bin/evn python
#coding=utf-8


import os, sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from flask_script import Manager, Server

from Blog import create_app
app = create_app