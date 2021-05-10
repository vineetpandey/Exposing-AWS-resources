from flask import Flask


app = Flask(__name__)
#  A secret key is required to use CSRF protection.
app.config['SECRET_KEY'] = 'c3485172fddc76f05434df6aa29a4e0d'

from flask_aws import routes