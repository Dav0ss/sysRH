from flask import Blueprint, render_template, session, url_for, redirect

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login')
def login():
    return 'Login page'