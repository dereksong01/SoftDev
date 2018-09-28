# Team Solo_Gudetama - Derek Song
# Soft Dev - PD8
# K#10 - Jinja Tuning
# 2018 - 09 - 23

import csv
from flask import Flask, render_template
from util import functions

app = Flask(__name__)

occDict = functions.convertor()
randOcc = functions.randOcc()
        
@app.route("/occupations")
def display():
    randome = randOcc
    return render_template("yes.html", occupationDict = occDict, rand = randome)

if __name__ == "__main__":
    app.debug = True
    app.run()
