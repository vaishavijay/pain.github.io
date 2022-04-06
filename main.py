from flask import render_template

# create a Flask instance
app = Flask(__name__)


@app.route("/")
# map URL route for function below
def index():
    return render_template("index.html")
  
def authorize():
    return render_template("authorize.html")
#Pranavi and Gigi
