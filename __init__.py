# Pranavi and Gigi

from flask_login import LoginManager

# The most important part of an application that uses Flask-Login is the LoginManager class.
# You should create one for your application like this:
# Setup LoginManager object (app)
login_manager = LoginManager()

# The login manager contains the code that lets your application and Flask-Login work together,
# such as how to load a user from an ID,  where to send users when they need to log in, and the like.
# Once the actual application object has been created, you can configure it for login with:

login_manager.init_app(app)
