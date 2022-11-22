from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
app = Flask(__name__)

app.config['SECRET_KEY'] ='secret'
#################################
#     Ruotes Public Interface
#################################
@app.route('/')
def index():
    return render_template('public/index.html')

@app.route('/about')
def about():
    return render_template('public/about.html')
@app.route('/contact')
def contact():
    return render_template('public/contact.html')

@app.route('/portal')
def portalfolio():
    projects = [ 
        {
        'name': 'First Project',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Saepe nostrum ullam eveniet pariatur voluptates odit, fuga atque ea nobis sit solutaodio, adipisci quas excepturi maxime quae totam ducimus consectetur?',
        'image': 'img/home-bg.jpg',
        'url': 'https://www.youtube.com'
        },
        {
        'name': 'Second Project',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Saepe nostrum ullam eveniet pariatur voluptates odit, fuga atque ea nobis sit solutaodio, adipisci quas excepturi maxime quae totam ducimus consectetur?',
        'image': 'img/about-bg.jpg',
        'url': 'https://www.github.com'
        },
        
    ]
    return render_template('public/portfolio.html', projects=projects)


################################
#           Form WTFroms
################################

class LoginFrom(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    submit = SubmitField('Ingresar')

################################
#           Routes Login
################################

@app.route('/auth/login')
def login():
    form = LoginFrom()
    return render_template('auth/login.html', form=form)
@app.route('/auth/register')
def register():
    return render_template('auth/register.html')

@app.route('/welcome', methods=['GET','POST'])
def welcome():
    email = request.form['mail']
    password = request.form['password']
    access = {'email':email}

    return render_template('admin/index.html', user_access=access)

@app.errorhandler(404)
def page_error_not_found(e):
    return render_template('error/404.html'), 404
if __name__ == '__main__':
    app.run(debug=True)