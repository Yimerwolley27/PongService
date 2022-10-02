from multiprocessing import AuthenticationError
import os
from flask import Flask, jsonify 
from flask_sqlalchemy import SQLAlchemy
import requests
from flask_httpauth import HTTPDigestAuth
import random
import functions_framework

URL = 'http://127.0.0.1:5000/'

#create a Flask application instance called app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secrey key here'
auth = HTTPDigestAuth()
users = {'vcu': 'rams'}

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'message': 'Page Doesnt Work'}), 404


@app.route('/pong', methods=['GET'])
@auth.login_required
@functions_framework.http
def pong():
    randomNum = random.randint(1, 100)
    output = {"randoly generated integer": randomNum}
    return jsonify(output) 
