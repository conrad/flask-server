from app import app
from flask import render_template

@app.route('/')
def hello():
    return "Hello, World!"
@app.route('/index')
def index():
    user = {'nickname': 'MC'}
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in SF!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Cumberbatch movie was so cool!'
        },
        {
            'author': {'nickname': 'Clark'},
            'body': 'Let\'s go for a sail!'
        }
    ]
    return render_template('index.html',
                            title='Home',
                            user=user,
                            posts=posts)
