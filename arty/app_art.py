import markdown
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from cruddy.query import user_by_id
from cruddy.model import Art

# blueprint defaults https://flask.palletsprojects.com/en/2.0.x/api/#blueprint-objects
app_art = Blueprint('art', __name__,
                      url_prefix='/art',
                      template_folder='templates/arty/',
                      static_folder='static',
                      static_url_path='static')


@app_art.route('/art')
@login_required
def art():
    # defaults are empty, in case user data not found
    user = ""
    list_art = []

    # grab user database object based on current login
    uo = user_by_id(current_user.userID)

    # if user object is found
    if uo is not None:
        user = uo.read()  # extract user record (Dictionary)
        for draw in uo.notes:  # loop through each user note
            draw = draw.read()  # extract note record (Dictionary)
            draw['note'] = markdown.markdown(draw['note'])  # convert markdown to html
            list_art.append(draw)  # prepare note list for render_template
        if list_art is not None:
            list_art.reverse()
    # render user and note data in reverse chronological order
    return render_template('art.html', user=user, art=list_art)


# Notes create/add
@app_art.route('/create/', methods=["POST"])
@login_required
def create():

    """gets data from form and add to Notes table"""
    if request.form:
        # construct a Notes object
        draw_object = Art(
            request.form.get("art"), current_user.userID
        )
        # create a record in the Notes table with the Notes object
        draw_object.create()
    return redirect(url_for('art.art'))

