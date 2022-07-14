from flask import render_template, request
from app import db, login_manager
from app.errors import error


@login_manager.unauthorized_handler
def unauthorized_handler():
    return render_template('errors/page-403.html'), 403

@error.app_errorhandler(404)
def not_found_error(e):
    return render_template('errors/page-404.html'), 404


@error.app_errorhandler(500)
def internal_error(e):
    return render_template('errors/page-500.html'), 500







