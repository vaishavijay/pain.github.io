import os
from __init__ import app
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename

from cruddy.query import user_by_id

# blueprint defaults https://flask.palletsprojects.com/en/2.0.x/api/#blueprint-objects
app_art = Blueprint('art', __name__,
                        url_prefix='/art',
                        template_folder='templates/arty/',
                        static_folder='static',
                        static_url_path='static')

''' 
Objective of the ideas started with this page is to manage uploading content to a Web Site
Code provided allows user to upload Image into static/uploads folder 
'''
# ... An Image is often called a picture, it works with <image ...> tage in HTML
# ... Supported types jpeg, gif, png, apng, svg, bmp, bmp ico, png ico.

'''
Hack #1 add additional content
'''
# Additional Content
# ... Video, Comma Seperated Values (CSV), Code File (py,java)
# ... One or more uploading capabilities can be provided to support needs of your project

'''
Hack #2 add additional description and capabilities
'''
# Establish a database record that keeps track of content and establishes meta data
# ... user who uploaded
# ... description
# Combine Note and Image upload into single activie
# ... description of Note is Markdown text
# ... try using uploaded image in notes
# ... think about easier markdown UI for user of Note and Images

'''
Hack #3 establish a strategy to manage data being stored through Amazon S3 bucket
'''
# AWS S3 Object Container is a system used to manage content
# ... S3 Bucket Concept: https://www.youtube.com/watch?v=-VVC7uTNJX8


# A global variable is used to provide feedback for session to users, but is considered short term solution
files_uploaded = []


def upload_save(file_object):
    # set path to location defined in __init__.py
    path = app.config['UPLOAD_FOLDER']
    if not os.path.exists(path):
        # Create a new directory because it does not exist
        os.makedirs(path)

    # secure_filename checks for integrity of filename, avoids hacking
    filename = secure_filename(file_object.filename)
    # os.path.join adds path for uploads
    upload_location = os.path.join(path, filename)
    # save file object to upload location
    file_object.save(upload_location)
    return filename


# Page to upload content page
@app_art.route('/')
@login_required
def art():
    # grab user object (uo) based on current login
    uo = user_by_id(current_user.userID)
    user = uo.read()  # extract user record (Dictionary)
    # load content page
    return render_template('art.html', user=user, files=files_uploaded)


@app_art.route('/delete/', methods=["POST"])
def delete():
    if request.form:
        path = '/drawing/<name>'
        if os.path.exists(path):
            os.remove(path)

    return redirect(url_for('art.art'))


# Notes create/add
@app_art.route('/upload/', methods=["POST"])
@login_required
def upload():
    try:
        # grab file object (fo) from user input The fo variable holds the submitted file object. This is an instance
        # of class FileStorage, which Flask imports from Werkzeug.
        fo = request.files['filename']
        filename = upload_save(fo)

        # inserts location of object to feedback list
        files_uploaded.insert(0, url_for('uploads_endpoint', name=filename))
    except:
        # errors handled, but specific errors are not messaged to user
        pass
    # reload content page
    return redirect(url_for('art.art'))