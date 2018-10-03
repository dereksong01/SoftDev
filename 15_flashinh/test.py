#Team Derek - Derek Chan and Derek Song
#SoftDev1 pd8
#K14 -- Do I Know You?
#2018-10-02
import os
from flask import Flask, render_template, request, session, redirect, url_for
app = Flask(__name__)

app.secret_key = os.urandom(32) #set the secret key
test_user = {'chan' : 'song'} #make the hard coded user and password

@app.route('/')
def index():
    return render_template("login.html") #login page

@app.route("/auth", methods = ["POST"])
def login():
    if request.form['username'] in test_user: #sees if the username is correct
        if request.form['password'] == test_user['chan']: #sees if the password for the username is correct
            session[request.form['username']] = request.form['password'] #creates the session only if password and username are correct
            return render_template('welcome.html', user = request.form['username']) #returns a welcome if password and username are correct
        return render_template('denied.html', user = request.form['username'], error = 'has a incorrect password') #returns a password error if only the username is recognized
    return render_template('denied.html', user = request.form['username'], error = 'is unrecognized') #everything is wrong

@app.route("/logout")
def logout():
    if 'chan' in session:
        session.pop('chan') #ends the session and redirects back to login page
    return redirect(url_for("index")) #goes back to the login page 

@app.route("/test") #used to test if the session is remembered
def test():
    if 'chan' in session:
        return "yup you are logged in"
    return "sorry bro ya not logged in"


app.debug = True
app.run()
