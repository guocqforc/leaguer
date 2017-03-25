#coding:utf8
from flask import blueprints, render_template


bp = blueprints('frontend', __name__)

@bp.route('/')
def index():
    return render_template('/frontend/index.html')