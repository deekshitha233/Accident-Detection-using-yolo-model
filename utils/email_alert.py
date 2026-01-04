from flask_mail import Mail, Message
from flask import Flask


app = Flask(__name__)


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'deekshithavundavallimailid@gmail.com'
app.config['MAIL_PASSWORD'] = 'pyf'


mail = Mail(app)


def send_email():
 with app.app_context():
    msg = Message('Accident Alert', sender='deekshithavundavallimailid@gmail.com', recipients=['deekshithavundavallimailid@gmail.com'])
    msg.body = '🚨 Accident detected by YOLOv8 system.'
    mail.send(msg)