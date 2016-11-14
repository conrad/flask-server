from app import app
from flask import render_template, redirect, flash
from .forms import LoginForm

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested fro OpenID="%s", remember_me=%s' %
            (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                            title='Sign In',
                            form=form
                            providers=app.config['OPENID_PROVIDERS'])
