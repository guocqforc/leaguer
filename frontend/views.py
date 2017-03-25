#coding:utf8
from flask import Blueprint, render_template


bp = Blueprint('frontend', __name__)

@bp.route('/')
def index():
    return render_template('/frontend/index.html')