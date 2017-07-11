# -*-coding:utf-8 -*-
from . import main
from flask import render_template, session
from .views import Kjhm

kjxx = Kjhm.getkjhmbycount()
pageinfo = {"nowpage": 1, 'totalpage': Kjhm.pagenum()}


@main.app_errorhandler(404)
def page_not_found(e):

    return render_template('404.html', pageinfo=pageinfo, username=session['username'], user_id=session['user_id'], kjxx=kjxx, topxx=kjxx[0], botxx=kjxx[-1]), 404


@main.app_errorhandler(500)
def page_not_found(e):
    kjxx = Kjhm.getkjhmbycount()
    return render_template('404.html', pageinfo=pageinfo, username=session['username'], user_id=session['user_id'], kjxx=kjxx, topxx=kjxx[0], botxx=kjxx[-1]), 500



