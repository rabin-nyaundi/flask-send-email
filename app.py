import os

from flask import Flask, request, render_template, url_for
from flask_mail import Mail, Message

app = Flask(__name__)

mail = Mail(app)


app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'your email address'
app.config['MAIL_DEFAULT_SENDER'] = 'your email address'
app.config['MAIL_PASSWORD'] = '*******'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
            
        email = request.form.get('email')
        message = request.form.get('message')
        name = request.form.get('name')
        
        msg = Message('Your Subject here', recipients = ['recipient email address'])        
        msg.html = '<br> Hello name,<br>'+ message + '<br><br> Kind regards<br>' + name
        mail.send(msg)
        
        return 'Sent Successfully'
    
    return render_template('index.html')
   


if __name__ == '__main__':
   app.run(debug = True)
   