# -*-coding:utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms import ValidationError
from ..models import User


class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()])
    password = PasswordField('密　码', validators=[DataRequired()])
    submit = SubmitField('登　陆')


class RegisterForm(FlaskForm):
    username = StringField('　用户名', validators=[DataRequired()])
    password = PasswordField('　密　码', validators=[DataRequired(), EqualTo('password2', message='密码必须一致')])
    password2 = PasswordField('确认密码', validators=[DataRequired()])
    email = StringField('　邮　箱', validators=[Email(), Length(1, 30)])
    # email = StringField('　邮　箱', validators=[DataRequired(), Email(), Length(1, 30)])
    address = StringField('　地　址')
    submit = SubmitField('注　册')

