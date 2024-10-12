from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, InputRequired, EqualTo, Regexp
import os

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

# A common regex for validating email addresses
email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(),Regexp(regex=email_regex, flags=0, message=None) ])
    password = PasswordField('New Password', [InputRequired()])
    submit = SubmitField('Log in')

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY') 

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template('login.html', form=login_form)

if __name__ == '__main__':
    app.run(debug=True)
