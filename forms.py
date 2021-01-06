from flask_wtf import Form
from wtforms import validators, StringField, PasswordField, TextField, SubmitField
from wtforms.fields.html5 import EmailField

class SignUp_Form(Form):
    username = StringField('Username', [
        validators.Required(message = 'Your username is required'),
        validators.length(min=4, max=25, message='Please enter a valid user name')]
        )

    firstname = StringField('Firstname', [
        validators.Required(message = 'Your name is required'), 
        validators.length(min=4, max=25, message='Please enter a valid name')]
        )

    lastname = StringField('Lastname', [
        validators.Required(message = 'Your last name is required'), 
        validators.length(min=4, max=25, message='Please enter a valid last name')]
        )

    email = EmailField('Email', [
        validators.Required(message='The mail is required'), 
        validators.Email(message='Enter a valid email')]
        )

    password = PasswordField('Password', [
        validators.Required(message = 'password is required')
    ])

    submit = SubmitField('Send')


class Login_Form(Form):
    email = EmailField('email', [
        validators.Required(message='The mail is required'), 
        validators.Email(message='Enter a valid email')]
        )

    password = PasswordField('password', [
        validators.Required(message = 'password is required')])

    enviar = SubmitField('Log in')


class Search_Form(Form):
    city = StringField('City name', [
        validators.Required(message = 'The name of the city is required'),
        validators.length(min = 4, max = 25, message = 'Enter a valid city')
    ])

    submit = SubmitField('Get weather')