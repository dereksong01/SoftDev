#Team Derek - Derek Chan and Derek Song
#SoftDev1 pd8
#K15 -- Oh yes, perhaps I do…
#2018-10-03
import os
from flask import Flask, render_template, request, session, redirect, url_for, flash
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
            flash('Welcome '+ request.form['username'] +', how are you?')
            return render_template('welcome.html', title = 'Welcome') #returns a welcome if password and username are correct
        flash('Sorry '+ request.form['username'] +', has a incorrect password')
        return render_template('welcome.html', title = 'ERROR') #returns a password error if only the username is recognized
    flash('Sorry '+ request.form['username'] +', is unrecognized')
    return render_template('welcome.html', title = 'ERROR') #everything is wrong

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
