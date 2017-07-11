# -*-coding:utf-8 -*-
from flask import render_template, url_for, redirect, flash, session, json, request
from .. import connection
from . import main
from .forms import LoginForm, RegisterForm
from ..models import User, Kjhm


@main.route('/', methods=['GET', 'POST'])
def first():
    Kjhm.get_kjhm_and_weather_by_count()
    kjxx = Kjhm.getkjhmbycount()
    pageinfo = {"nowpage": 1, 'totalpage': Kjhm.pagenum()}
    if 'username' and 'user_id' not in session.keys():
        session['username'] = "游客"
        session['user_id'] = 5
    return render_template('index.html', pageinfo=pageinfo, username=session['username'], user_id=session['user_id'],
                           kjxx=kjxx, topxx=kjxx[0], botxx=kjxx[-1])


@main.route('/select_condition', methods=['POST'])
def select_condition():
    ball_color = request.values.get("ball_color")
    select_condition = request.values.get("select_condition")
    ball = request.values.get("ball")


@main.route('/get_kjxx', methods=['GET', 'POST'])
def get_kjxx():
    pagesize = 30
    nowpage = int(request.args.get('nowpage'))
    ball_color = request.values.get("ball_color")
    select_condition = request.values.get("select_condition")
    ball = request.values.get("ball")

    flag = False
    if ball_color and select_condition is not None:
        flag = True
    if nowpage <= 0:
        nowpage = 0
    elif nowpage >= Kjhm.pagenum():
        nowpage = Kjhm.pagenum() - 1
    action = request.args.get('action')
    if action == 'uppage':
        kjxx = Kjhm.getkjhmbycount(start=pagesize*(nowpage-2), end=pagesize)
        nowpage = nowpage - 1
    elif action == 'nextpage':
        kjxx = Kjhm.getkjhmbycount(start=pagesize*nowpage, end=pagesize)
        nowpage = nowpage + 1

    pageinfo = {"nowpage":nowpage, 'totalpage':Kjhm.pagenum()}
    return render_template('index.html', pageinfo=pageinfo, username=session['username'], user_id=session['user_id'],
                           kjxx=kjxx, topxx=kjxx[0], botxx=kjxx[-1]), 200


@main.route('/plot_bar', methods=['GET', 'POST'])
def plot_index():
    kjxx = Kjhm.getkjhmbycount()
    pageinfo = {"nowpage": 1, 'totalpage': Kjhm.pagenum()}
    return render_template('tables/count_of_ball.html')


@main.route('/plot_weather', methods=['GET', 'POST'])
def plot_weather():
    return render_template('tables/weather_and_ball.html')


@main.route('/blue_pic_bar', methods=['GET', 'POST'])
def blue_pic_bar():
    return render_template('tables/blue_Pic_bar.html')


@main.route('/blue_pic_scatter', methods=['GET', 'POST'])
def blue_pic_scatter():
    return render_template('tables/blue_pic_scatter.html')


@main.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.getuserbyname(name=form.username.data)
        if user is not None and user.verify_password(form.password.data):
            # CheckLoginUser.set_login_user(user)
            session['username'] = user.username
            session['user_id'] = user.id
            return redirect(url_for('main.first'))
            return render_template('index.html')
        flash("用户名或密码错误")
    return render_template('login.html', form=form, username=session['username'], user_id=session['user_id'])


@main.route('/logout', methods=['GET', 'POST'])
def logout():
    session['username'] = "游客"
    session['user_id'] = 5
    return redirect(url_for('main.first'))


@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        password = form.password.data
        password2 = form.password2.data
        username = form.username.data
        email = form.email.data
        address = form.address.data
        roleid = 4
        user = User(username=username, email=email, address=address, role_id=roleid, password_hash=password)
        user_temp = User.getuserbyname(name=username)

        if user_temp is not None:
            flash("用户名已存在")
            return render_template('register.html', form=form)
        # 设置password
        user.__setattr__('password', password)
        User.insertuser(user)
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form, username=session['username'], user_id=session['user_id'])





