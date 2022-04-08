# Pranavi and Gigi
from flask import render_template
from __init__ import app

from cruddy.app_crud import app_crud
from cruddy.app_crud_api import app_crud_api

app.register_blueprint(app_crud)
app.register_blueprint(app_crud_api)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/authorize')
def authorize():
    return render_template("authorize.html")


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(
        host='0.0.0.0',
        debug=True,
        port=8080
    )