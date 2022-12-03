from flask import Flask, redirect, render_template, request, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField,
EmailField, IntegerField, RadioField, SelectField, TextAreaField)
from wtforms.validators import  DataRequired, Email


########## Nuestros modulos ###########
from home.views import home_blueprint
from auth.views import auth_blueprint
app = Flask(__name__)

app.config['SECRET_KEY'] ='secret'




@app.errorhandler(404)
def page_error_not_found(e):
    return render_template('error/404.html'), 404


################### app ##################

app.register_blueprint(home_blueprint, url_prefix='/')
app.register_blueprint(auth_blueprint, url_prefix='/auth')

if __name__ == '__main__':
    app.run(debug=True)