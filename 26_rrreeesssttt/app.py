# Derek Song
# SoftDev1 pd8
# K25 -- Getting More REST
# 2018 - 11 - 15

from flask import Flask, render_template
import urllib, json

app = Flask(__name__)

@app.route("/")
def inform_user():
    KEY_NDB = "hjmklcFuCL8zkX8MTENIODUAZGPFgTlddwDJxGZ2" # API Key
    URL_STUB = "https://developer.nrel.gov/api/alt-fuel-stations/v1/nearest.json?api_key=" # USDA
    ext = "&location=Denver+CO" # Extension for example URL
    url = URL_STUB + KEY_NDB + ext
    print(url)
    #x = urllib.request.urlopen('https://api.nasa.gov/planetary/apod?api_key=motrt4z0moLTYLk3ziqhyD8KCZsf6k4n8EwJcBN0').read()
    return render_template('index.html')

if __name__ == "__main__":
    app.debug = True
    app.run()
