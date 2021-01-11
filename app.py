from flask import Flask,redirect,url_for,render_template,request,flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_wtf import CSRFProtect

import requests
import forms

from config import DevelopmentConfig, ProductionConfig
from models import db, User

app = Flask(__name__)
app.config.from_object(ProductionConfig)
Bootstrap(app)
csrf = CSRFProtect()

def weather_JSON(city):
    API_Key = '22b171bd64df6212a8a495bbf801e05a'
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    parameters = {
        'appid': API_Key,
        'q': city,
        'units': 'metric'
    }
    reply = requests.get(URL, params = parameters)
    var_weather = reply.json()
    return var_weather


@app.before_request
def before_request():
    if 'username' not in session and request.endpoint in ['weather_world', 'logout']:
        return redirect( url_for('home') )
    elif 'username' in session and request.endpoint in ['login', 'registrarse']:
        return redirect( url_for('home') )


@app.route('/',methods=['GET','POST'])
def home():
    login_form = forms.Login_Form()
    if request.method=='POST':
        # Handle POST Request here
        return render_template('index.html')
    return render_template('index.html', form = login_form)


@app.route("/weather-world/", methods = ["GET", "POST"])
def weather_world():
    weather_form = forms.Search_Form()

    if request.method == "POST" and weather_form.validate():
        city = weather_form.city.data
        
        return render_template('weather2.html', var_weather = weather_JSON(city))

    return render_template('weather.html', form = weather_form)


@app.route("/login", methods = ['GEt', 'POST'])
def login():
    login_form = forms.Login_Form(request.form)

    if request.method == "POST" and login_form.validate():
        email = login_form.email.data
        password = login_form.password.data

        user = User.query.filter_by(email = email).first()

        if user is not None and user.verify_password(password):
            success_message = f'Wellcome {user.username}'
            flash(success_message)
        else:
            success_message = 'Invalid username or password'
            flash(success_message)

        session['username'] = user.username

    return render_template('login.html', form = login_form)


@app.route("/signup", methods = ['GEt', 'POST'])
def signup():
    signup_form = forms.SignUp_Form(request.form)
    if request.method == "POST" and signup_form.validate():
        u = User(
            username = signup_form.username.data,
            firstname = signup_form.firstname.data,
            lastname = signup_form.lastname.data,
            email = signup_form.email.data,
            password = signup_form.password.data)

        print(u)
        db.session.add(u)
        db.session.commit()

        success_message = "Successfully registered user"
        flash(success_message)

    return render_template('signup.html', form = signup_form)


@app.route("/logout")
def logout():
    if 'username' in session:
        session.pop('username')
    return redirect(url_for('login'))


if __name__ == '__main__':
    db.init_app(app)
    csrf.init_app(app)

    with app.app_context():
        db.create_all()

    app.run()