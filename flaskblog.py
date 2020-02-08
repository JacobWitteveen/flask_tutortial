'''
Need to run the following in a cmd (not powershell)
>FLASK_APP = flaskblog.py
>flask run

# to set debugging
# allows for changes to be pushed to localhost without quitting the app and restarting
set FLASK_DEBUG=1

- flask run uses the env vars we set, adding if __name__ cond allows script to be run in python
- Look into flask bootstrap vs just using the bootstrap general
- SECRET_KEY protects from cookie issues, generated key using secrets.token_hex(16) python command
'''


from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

# __name__ is the name of the module
app = Flask(__name__)
app.config['SECRET_KEY'] ='459d0a254cb937ef30145e086a78973c'

posts = [
    {
        'author': 'Jake Witt',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

# routes are what we type in the browser
@app.route('/')
@app.route('/home') # both routes return function below
def home():
    return render_template('home.html', posts=posts)

# routes are what we type in the browser
@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)

'''
https://www.youtube.com/watch?v=QnDWIZuWYW0 stopped at 10:40
'''