from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'schandenfreude'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '2525'
app.config['MAIL_USERNAME'] = ' user567'
app.config['MAIL_PASSWORD'] = 'pass001'

mail = Mail(app)
from app import views
