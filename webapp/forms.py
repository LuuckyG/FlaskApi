from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo

from webapp.models import User


class LoginForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class SearchForm(FlaskForm):
    project_titel = StringField('Projecttitel')
    zwaartepunt = StringField('Zwaartepunt')
    key_terms = StringField('Key terms')
    aanleiding = StringField('Aanleiding')
    t_knel = StringField('Technische knelpunten')
    opl = StringField('Oplossingsrichting')
    prog = StringField('Programmeertalen, ontwikkelomgevingen en tools')
    nieuw = StringField('Waarom technisch nieuw')
    submit = SubmitField('Zoek aanvragen!')
