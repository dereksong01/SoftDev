# Derek Song
# Soft Dev - PD8
# K#08 - Fill Yer Flask
# 2018 - 9 - 19

from flask import Flask
app = Flask(__name__) #instantiates the Flask class using a constructor

@app.route('/')
def home0():
        print(__name__)
	return 'No'

@app.route('/0')
def home1():
        print(__name__)
        return 'Hablo'

@app.route('/1')
def home2():
        print(__name)
        return 'Queso'


app.debug = True
app.run()
