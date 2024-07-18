from flask import Flask, render_template, url_for, request, redirect,flash
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from datetime import datetime
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField,SubmitField, EmailField, TelField, BooleanField
from wtforms.validators import Email, Length, DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'PleaseChageMe'

@app.route('/', methods=['POST', 'GET'])
@app.route('/home', methods=['POST', 'GET'])
def main():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)
