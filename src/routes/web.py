import functools
from flask import Blueprint, jsonify, render_template

bp = Blueprint('web', __name__)
# Applications Route

@bp.route('/')
def index():
    return render_template("welcome.html")