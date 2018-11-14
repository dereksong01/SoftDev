# Team astro0 - Derek Song and Zane Wang
# SoftDev1 pd8
# K24 -- A RESTful Journey Skyward
# 2018 - 11 - 13

from flask import Flask, render_template
import urllib, json

app = Flask(__name__)

@app.route("/")
def inform_user():
    x = urllib.request.urlopen('https://api.nasa.gov/planetary/apod?api_key=motrt4z0moLTYLk3ziqhyD8KCZsf6k4n8EwJcBN0').read()
    return render_template('index.html', pic = x)

if __name__ == "__main__":
    app.debug = True
    app.run()
