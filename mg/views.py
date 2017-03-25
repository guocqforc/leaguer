#coding:utf8

from flask import Blueprint

bp = Blueprint('mg', __name__)

@bp.route('/mg')
def index():
    pass