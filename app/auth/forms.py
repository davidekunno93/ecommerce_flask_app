from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length

class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=4)])
    email = StringField("Email", validators=[DataRequired(), Length(min=4)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=4)])
    confirm_password = PasswordField("ConfirmPassword", validators=[DataRequired(), EqualTo("password")])
    register = SubmitField("Register")

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=4)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=4)])
    login = SubmitField("Login")