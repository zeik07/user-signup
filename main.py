from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/", methods=['POST'])
def signup():
    error=False
    username_error = ""
    verify_error = ""
    email_error = ""
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']
    if len(username) < 3:
        username_error = "Username is too short.".format(username)
        error=True
    elif len(username) > 20:
        username_error = "Username is too long.".format(username)
        error=True
    elif " " in username:
        username_error = "Username can't contain a space.".format(username)
        error=True

    if len(password) < 3 or len(password) > 20 or " " in password:
        password_error = "Not a valid password."
        error=True

    if password != verify:
        verify_error = "Passwords do not match.".format(verify)
        error=True

    if "@" not in email and "." not in email:
        if email != "":
            email_error = "Not a valid email address.".format(email)
            error=True
    
    if error == True:
        return render_template('index.html' , username=username , username_error=username_error , password_error=password_error , verify_error=verify_error , email=email , email_error=email_error)

    return render_template('welcome.html' , username=username)

@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('index.html', error=encoded_error and cgi.escape(encoded_error, quote=True))

app.run()