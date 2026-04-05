from flask import render_template, url_for, request, redirect, session

from . import bp

@bp.route('/')
def main():
    return render_template('main.html')

