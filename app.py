# Derek Song
# Soft Dev - PD8
#
# 2018 - 09 - 27

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def display():
    return render_template("test.html")

@app.route("/auth")
def authenticate():
    print(app)
    print(request)
    print(request.headers)
    print(request.method)
    print(request.args)
    print(request.form)

#if __name__ == ("__main__"):
app.debug = True
app.run()
