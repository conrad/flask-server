# Setup
While at root of project, create virtual environment from terminal:
    - mac with Python 3.4+ : $ python -m venv flask
    - mac with older Python: $ sudo easy_install virtualenv
    - linux: $ sudo apt-get install python-virtualenv
    - windows:
        (1) Install pip
        (2) $ pip install virtualenv
        (3) $ virtualenv flask

Install dependencies:
    - mac & linux: $ flask/bin/pip install flask
    - windows: $ flask\Scripts\pip install flask

# Running the Server
To run the server, $ ./run.py

# List of Dependencies
Dependencies intended to be installed as this progresses:
$ flask/bin/pip install flask    # Already installed, required for server
$ flask/bin/pip install flask-login
$ flask/bin/pip install flask-openid
$ flask/bin/pip install flask-mail
$ flask/bin/pip install flask-sqlalchemy
$ flask/bin/pip install sqlalchemy-migrate
$ flask/bin/pip install flask-whooshalchemy
$ flask/bin/pip install flask-wtf   # Needed for web forms
$ flask/bin/pip install flask-babel
$ flask/bin/pip install guess_language
$ flask/bin/pip install flipflop
$ flask/bin/pip install coverage
