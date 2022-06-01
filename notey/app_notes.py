import markdown
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from cruddy.query import user_by_id
from cruddy.model import Notes
from arty.app_art import upload_save

# blueprint defaults https://flask.palletsprojects.com/en/2.0.x/api/#blueprint-objects
app_notes = Blueprint('notes', __name__,
                      url_prefix='/notes',
                      template_folder='templates/notey/',
                      static_folder='static',
                      static_url_path='static')


def notes_display(uo):  # uo is user object
    # defaults are empty, in case user data not found
    user = ""
    list_notes = []

    # if user object is found
    if uo is not None:
        user = uo.read()  # extract user record (Dictionary)
        for note in uo.notes:  # loop through each user note
            note = note.read()  # extract note record (Dictionary)
            note['note'] = markdown.markdown(note['note'])  # convert markdown to html
            list_notes.append(note)  # prepare note list for render_template
        if list_notes is not None:
            list_notes.reverse()
    # render user and note data in reverse chronological order
    return render_template('notes.html', user=user, notes=list_notes)


@app_notes.route('/')
@login_required
def notes():
    # grab user database object based on current login
    uo = user_by_id(current_user.userID)
    return notes_display(uo)


@app_notes.route('/notes_select<userID>')
@login_required
def notes_select(userID):
    # grab user database object based on current login
    uo = user_by_id(userID)
    return notes_display(uo)

# Notes create/add
@app_notes.route('/create/', methods=["POST"])
@login_required
def create():
    """gets data from form and add to Notes table"""
    if request.form:
        # construct a Notes object
        fo = request.files['filename']
        filename = upload_save(fo)
        note_object = Notes(
            current_user.userID,
            request.form.get("notes"),
            filename
        )
        # create a record in the Notes table with the Notes object
        note_object.create()
    return redirect(url_for('notes.notes'))
