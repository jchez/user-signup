from flask import Flask, request, redirect
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader 
(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    template = jinja_env.get_template('home.html')
    return template.render()

@app.route("/", methods = ['POST'])
def validate_info():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    if " " in username or len(username) < 3 or len(username) > 20:
        username_error = "That's not a valid username"

    if " " in password or len(password) < 3 or len(password) > 20:
        password_error = "That's not a valid password"

    if password != verify_password:
        verify_error = "Passwords don't match"

    if "@" not in email or "." not in email or email.count(".") > 1 or email.count("@") > 1 or " " in email or len(email) < 3 or len(email) > 20:
        email_error = "That's not a valid email"

    if not username_error and not password_error and not verify_error and not email_error:
        return "hello"

    else:
        template = jinja_env.get_template('home.html')
        return template.render(username=username,
            email = email,
            username_error=username_error,
            password_error = password_error,
            verify_error = verify_error,
            email_error = email_error)

@app.route("/welcome", methods=['POST'])
def welcome():
    username = request.form['username']
    template = jinja_env.get_template('welcome.html')
    return template.render(name=username)

app.run()