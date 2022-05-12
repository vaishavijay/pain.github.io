# Pranavi and Gigi
from flask import render_template
from __init__ import app

from cruddy.app_crud import app_crud
from cruddy.app_crud_api import app_crud_api
from notey.app_notes import app_notes


app.register_blueprint(app_crud)
app.register_blueprint(app_crud_api)
app.register_blueprint(app_notes)



@app.route('/')
def index():
    return render_template("index.html")

@app.route('/music')
def music():
    return render_template("music.html")

@app.route('/authorize')
def authorize():
    return render_template("authorize.html")

@app.route('/gmap')
def gmap():
    return render_template("gmap.html")





if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(
        host='0.0.0.0',
        debug=True,
        port=8080
    )