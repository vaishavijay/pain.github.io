from flask import render_template, request
from __init__ import app
import json
import requests
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


@app.route('/authorize')
def authorize():
    return render_template("authorize.html")

@app.route('/gmap')
def gmap():
    return render_template("gmap.html")

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


@app.route('/journal')
def journal():
    return render_template("journal.html")


if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(debug=True)