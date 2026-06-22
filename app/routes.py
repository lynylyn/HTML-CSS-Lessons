from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Juliet'}
    posts = [
        {
            'author': {'username': 'Emma'},
            'body': 'Huh?'
        },
        {
            'author': {'username': 'Onadi'},
            'body': 'Hi'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)