from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo
from exams.models import Users

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    register = SubmitField('Sign Up')

    def validate_username(self,username):
        user = Users.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('This username has been taken. Choose another one')

    def validate_email(self,email):
        user = Users.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('This email has been taken. Choose another one')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Email()])
    remember = BooleanField('Remember Me')
    login = SubmitField('Log In')

class QuizForm(FlaskForm):
    subject = StringField('Subject', validators=[DataRequired()])
    year = StringField('Year', validators=[DataRequired()])
    set_quiz = SubmitField('Set Quiz')

class QuestionForm(FlaskForm): 
    question = StringField('Question',validators=[DataRequired()])
    answers = StringField('Options',validators=[DataRequired()])
    post = SubmitField('Submit Questions')
