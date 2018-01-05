#might as well right this in Node

from flask import Flask, render_template
app = Flask(__name__, static_folder="static/dist", template_folder="static")

@app.route("/"):
   return render_template("index.html")

@app.route('/hello')
def hello_world():
   return('Hello, World!')

if __name__=="__main__":
   app.run()
