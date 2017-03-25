#coding:utf8
import flask_script
from  flask_script.commands import ShowUrls
from application import create_app

manager = flask_script.Manager(create_app())

if __name__ == '__main__':
    manager.run()

