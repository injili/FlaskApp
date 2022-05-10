from flask import Flask,request,render_template,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_bootstrap import Bootstrap


import os
import sqlite3
import flask

currentlocation = os.path.dirname(os.path.abspath(__file__))

myapp=Flask(__name__)
myapp.config['SECRET_KEY']='secret'
Bootstrap(myapp)

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=20)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    
class RegisterForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=20)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid Email'), Length(max=50)])    

@myapp.route('/')
def index():
    return render_template("index.html")

@myapp.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'
    return render_template('login.html', form = form)

@myapp.route('/signup', methods=['GET','POST'])
def signup():
    form = RegisterForm()   
    if form.validate_on_submit():
        return '<h1>' + form.username.data + ' ' + form.password.data + '</h>'
    return render_template("signup.html", form = form)

@myapp.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

if __name__ == '__main__':
    myapp.run(debug=True)