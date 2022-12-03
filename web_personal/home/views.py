from flask import Blueprint, render_template


home_blueprint = Blueprint('', __name__)
#################################
#     Ruotes Public Interface
#################################
@home_blueprint.route('/')
def index():
    return render_template('public/index.html')

@home_blueprint.route('/about')
def about():
    return render_template('public/about.html')
@home_blueprint.route('/contact')
def contact():
    return render_template('public/contact.html')

@home_blueprint.route('/portal')
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

