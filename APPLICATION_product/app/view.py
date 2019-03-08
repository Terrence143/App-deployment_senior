from app import app
from flask import render_template, request, redirect, url_for
from forms import LoginForm, RegisterEmployeeForm, EditForm
import requests
import json


@app.route('/', methods=['GET', 'POST'])
def index():
  form = LoginForm()
  if form.validate_on_submit():
    print form.username.data
    print form.password.data
    payload = {'username':form.username.data, 'password':form.password.data}
    r = requests.post('https://lit-woodland-64534.herokuapp.com/login', json = payload)
    r = r.json()
    if  r['message'] == 'Invalid username or password':
      error = 'Invalid username or password'
      return render_template('index.html', form=form, error=error)
    else:
      return redirect(url_for('home'))
  return render_template('index.html', form=form)

@app.route('/homepage', methods=['GET'])
def home():
  form = EditForm()
  data = requests.get('https://lit-woodland-64534.herokuapp.com/employee/all')
  data = data.json()
  return render_template('homepage.html', data=data, form=form)

@app.route('/add/employee', methods=['GET', 'POST'])
def register():
  form = RegisterEmployeeForm()
  if form.validate_on_submit():
    payload = {
    'firstname': form.firstname.data,
    'middlename': form.middlename.data,
    'lastname': form.lastname.data,
    'birthday': str(form.birthday.data),
    'gender': form.gender.data,
    'address': form.address.data,
    'nationality': form.nationality.data,
    'status': form.status.data,
    'code': form.code.data,
    'position': form.position.data
    }
    r = requests.post('https://lit-woodland-64534.herokuapp.com/add/employee', json = payload)
    r = r.json()
    if r['message'] == 'Employee was added Successfully!':
      return redirect(url_for('home'))
    else:
      error = r['message']
      return render_template('addemployee.html', form=form, error=error)
  return render_template('addemployee.html', form=form)

@app.route('/edit/employee', methods=['GET', 'POST'])
def edit_employee():
  form = EditForm()
  if form.validate_on_submit():
    payload = {
    'firstname': form.firstname.data,
    'middlename': form.middlename.data,
    'lastname': form.lastname.data,
    'birthday': str(form.birthday.data),
    'gender': form.gender.data,
    'address': form.address.data,
    'nationality': form.nationality.data,
    'status': form.status.data,
    'code': form.code.data,
    'position': form.position.data
    }
    r = requests.post('https://lit-woodland-64534.herokuapp.com/edit/employee/'+ form.code.data, json=payload)
    r = r.json()
    if r['message'] == 'Information was edited Successfully!':
      return redirect(url_for('home'))
  return redirect(url_for('home'))

@app.route('/view/removed', methods=['GET'])
def view_removed():
  data = requests.get('https://lit-woodland-64534.herokuapp.com/employee/deactivated')
  data = data.json()
  return render_template('removedemployee.html', data=data)

@app.route('/remove/<string:emp_code>', methods=['GET'])
def remove(emp_code):
  r = requests.get('https://lit-woodland-64534.herokuapp.com/remove/employee/' + emp_code)
  return redirect(url_for('home'))