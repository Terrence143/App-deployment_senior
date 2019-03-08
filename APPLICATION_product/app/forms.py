from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, ValidationError, SelectField, RadioField
from wtforms.fields.html5 import DateField
from wtforms.validators import Length, InputRequired, EqualTo, DataRequired, Email
import requests



class LoginForm(FlaskForm):
	username = StringField('Username', validators=[InputRequired(), Length(min=3, max=25)])
	password = PasswordField('Password', validators=[InputRequired(), Length(min=3, max=25)])

class RegisterEmployeeForm(FlaskForm):
	firstname = StringField('First name', validators=[InputRequired(), Length(min=3, max=25)])
	middlename = StringField('Middle name', validators=[InputRequired(), Length(min=3, max=25)])
	lastname = StringField('Last name', validators=[InputRequired(), Length(min=3, max=25)])
	birthday = DateField('Birth Date', format='%Y-%m-%d', validators=[DataRequired(), InputRequired()])
	gender = RadioField('Sex', validators=[InputRequired()], choices=[('Male', 'Male'), ('Female', 'Female')], default='Male')
	address = StringField('Complete Address', validators=[InputRequired(), Length(min=3, max=60)])
	code = StringField('Code', validators=[InputRequired(), Length(min=5, max=20)])
	position = StringField('Position', validators=[InputRequired(), Length(min=2, max=60)])
	status =  SelectField('Status', choices=[('Single', 'Single'), ('Married', 'Married'), ('Separated', 'Separated'), ('Widowed', 'Widowed'), ('Divorced', 'Divorced')])
	nationality = StringField('Nationality', validators=[InputRequired(), Length(min=3, max=30)])

class EditForm(FlaskForm):
	firstname = StringField('First name', validators=[InputRequired(), Length(min=3, max=25)])
	middlename = StringField('Middle name', validators=[InputRequired(), Length(min=3, max=25)])
	lastname = StringField('Last name', validators=[InputRequired(), Length(min=3, max=25)])
	birthday = DateField('Birth Date', format='%Y-%m-%d', validators=[DataRequired(), InputRequired()])
	gender = RadioField('Sex', validators=[InputRequired()], choices=[('Male', 'Male'), ('Female', 'Female')], default='Male')
	address = StringField('Complete Address', validators=[InputRequired(), Length(min=3, max=60)])
	code = StringField('Code', validators=[InputRequired(), Length(min=5, max=20)])
	position = StringField('Position', validators=[InputRequired(), Length(min=2, max=60)])
	status =  SelectField('Status', choices=[('Single', 'Single'), ('Married', 'Married'), ('Separated', 'Separated'), ('Widowed', 'Widowed'), ('Divorced', 'Divorced')])
	nationality = StringField('Nationality', validators=[InputRequired(), Length(min=3, max=30)])