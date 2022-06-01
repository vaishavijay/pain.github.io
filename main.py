from flask import render_template, redirect, request, url_for, send_from_directory
from flask_login import login_required
import json
from __init__ import app, login_manager
from cruddy.app_crud import app_crud
from cruddy.app_crud_api import app_crud_api
from notey.app_notes import app_notes
from arty.app_art import app_art

from cruddy.login import login, logout, signup

app.register_blueprint(app_crud)
app.register_blueprint(app_crud_api)
app.register_blueprint(app_notes)
app.register_blueprint(app_art)


@app.route('/')
def index():
    return render_template("index.html")


# Flask-Login directs unauthorised users to this unauthorized_handler
@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    app.config['NEXT_PAGE'] = request.endpoint
    return redirect(url_for('main_login'))


# if login url, show phones table only
@app.route('/login/', methods=["GET", "POST"])
def main_login():
    # obtains form inputs and fulfills login requirements
    global next_page
    if request.form:
        email = request.form.get("email")
        password = request.form.get("password")
        if login(email, password):
            try:  # try to redirect to next page
                next_page = app.config['NEXT_PAGE']
                app.config['NEXT_PAGE'] = None
                return redirect(url_for(next_page))
            except:  # any failure goes to home page
                return redirect(url_for('index'))

    # if not logged in, show the login page
    return render_template("login.html")


# if login url, show phones table only
@app.route('/logout/', methods=["GET", "POST"])
@login_required
def main_logout():
    logout()
    return redirect(url_for('index'))


@app.route('/authorize/', methods=["GET", "POST"])
def main_authorize():
    error_msg = ""
    # check form inputs and creates user
    if request.form:
        # validation should be in HTML
        user_name = request.form.get("user_name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")  # password should be verified
        if password1 == password2:
            if signup(user_name, email, phone, password1):
                return redirect(url_for('main_login'))
        else:
            error_msg = "Passwords do not match"
    # show the auth user page if the above fails for some reason
    return render_template("authorize.html", error_msg=error_msg)


@app.route('/drawing/<name>')
def uploads_endpoint(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)


# register "uploads_endpoint" endpoint so url_for will find all uploaded files
app.add_url_rule(
    "/" + app.config['UPLOAD_FOLDER'] + "/<name>", endpoint="uploads_endpoint", build_only=True
)


@app.route('/music')
def music():
    return render_template("music.html")


@app.route('/meditate')
def meditate():
    return render_template("meditate.html")


@app.route('/games')
def games():
    return render_template("games.html")


@app.route('/game1')
def game1():
    return render_template("game1.html")


@app.route('/game2')
def game2():
    return render_template("game2.html")


@app.route('/quiz')
def quiz():
    return render_template("quiz.html")


@app.route('/health')
def health():
    return render_template("health.html")


@app.route('/authorize')
def authorize():
    return render_template("authorize.html")


@app.route('/gmap')
def gmap():
    return render_template("gmap.html")


@app.route('/burnbook')
def burnbook():
    return render_template("burnbook.html")


# @app.route('/art')
# def art():
#    return render_template("arty/templates/art.html")

@app.route('/api')
def api():
    import requests
    url = "https://mental-health-info-api.p.rapidapi.com/news/thetimes"

    headers = {
        "X-RapidAPI-Host": "mental-health-info-api.p.rapidapi.com",
        "X-RapidAPI-Key": "4ab4681ba9mshf17197c9d59be44p17d1edjsnabe7ccc22eb5"
    }
    response = requests.request("GET", url, headers=headers)
    output = json.loads(response.text)
    print(response.text)
    return render_template("api.html", Z=output)


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


if __name__ == "__main__":
    # Replit required port, works on IntelliJ
    app.run(debug=False)
