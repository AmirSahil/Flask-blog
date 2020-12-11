from flask import Flask, request, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from models import User, Post


app = Flask(__name__)
app.config['SECRET_KEY'] = 'a6988613e1fa25983b7264f202c9e499'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


posts = [
    {
        'author' : 'Amir Sahil',
        'title' : 'Blog Post 1',
        'content' : 'First post content',
        'date_posted' : '12th December 2020'
    },
    {
        'author' : 'Dheeraj Ponnaganti',
        'title' : 'Blog Post 2',
        'content' : 'Secont post content',
        'date_posted' : '12th December 2020'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', blogposts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for { form.username.data }!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='login', form=form)

if __name__ == '__main__':
    app.run(debug = True)