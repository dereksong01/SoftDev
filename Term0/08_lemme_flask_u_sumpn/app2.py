from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return """
	<!DOCTYYPE html>
	<html>
	  <head>
	    <title></title>
	  </head>
	  <body>
	    Hello!
	  </body>
	</html>


"""

if __name__ == "__main__":
    app.debug = True
    app.run()
