from datetime import date, datetime
import numpy as np
import numpy_financial as npf

from flask import render_template, jsonify, request

from app.models import User

def calc_age(dob):
    born = datetime.strptime(dob, "%Y-%m-%d")
    today = datetime.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def home():
    return render_template('home.html')

def calculator():
    user = User.query.first()

    contrib_amount = int((user.salary / 100 * user.contribution) / 12) + int((user.salary / 100 * user.employer_contribution) / 12)

    retirement_year = (user.retirement_age - calc_age(user.dob)) + datetime.today().year

    future_value = npf.fv(0.07/12, (retirement_year-datetime.today().year)*12, -contrib_amount, -500)

    return render_template('calculator.html', employee_contrib=user.contribution, employer_contrib=user.employer_contribution, future_value="{:,}".format(round(future_value,2)), age=calc_age(user.dob))

def account():
    user = User.query.first()

    contrib_amount = int((user.salary / 100 * user.contribution) / 12)
    emp_contrib_amount = int((user.salary / 100 * user.employer_contribution) / 12)

    born = datetime.strptime(user.dob, "%Y-%m-%d")

    today = datetime.today()
    age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    return render_template('account.html', user=user, contrib_amount=contrib_amount, emp_contrib_amount=emp_contrib_amount, age=age)

def calc_fv():
    user = User.query.first()

    contrib_amount = int((user.salary / 100 * int(request.args['empe'])) / 12) + int((user.salary / 100 * int(request.args['empr'])) / 12)

    retirement_year = (user.retirement_age - int(request.args['age'])) + datetime.today().year

    future_value = npf.fv(0.07/12, (retirement_year-datetime.today().year)*12, -contrib_amount, -500)

    retirement_year_now = (user.retirement_age - calc_age(user.dob)) + datetime.today().year

    future_value_now = npf.fv(0.07/12, (retirement_year_now-datetime.today().year)*12, -contrib_amount, -500)

    return jsonify({'future_value_now': round(future_value_now,2), 'future_value': round(future_value,2)})