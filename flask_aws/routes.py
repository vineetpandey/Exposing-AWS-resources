from flask import render_template, url_for, flash, redirect
from flask_aws import app
from flask_aws.forms import RegistrationForm, LoginForm

from aws_resources.s3 import s3_public_via_policies
s3_public_via_policies.s3_public_check()
posts = [
    {
        # 'author': 'Vineet Pandey',
        'author': s3_public_via_policies.x,
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'Jan 11, 2020'
    },
    {
        'author': 'Robin Darwin',
        'title': 'Blog Post 12',
        'content': 'Second post content',
        'date_posted': 'Jan 14, 2020'
    }
]


@app.route('/')
@app.route('/home')
def  home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def  about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def  register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def  login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@vk.com' and form.password.data == 'pass':
            flash(f'You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
