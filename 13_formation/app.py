# Derek Song
# Soft Dev - PD8
# K#13 - Echo Echo Echo
# 2018 - 09 - 27

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def display():
    return render_template("home.html")

@app.route("/auth")
def authenticate():
    username = request.args['username']
    method = request.method
    return render_template("end.html", user = username, methodused = method)
    
    

if __name__ == ("__main__"):
    app.debug = True
    app.run()
