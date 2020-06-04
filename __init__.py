import os

from flask import Flask           #IMPORT FLASK CLASS

def create_app(test_config=None): #ALLOWS YOU TO ADD YOUR OWN CONFIG IF YOU WANT TO DO SOME AUTOMATED TESTING AGAINST WEB APP
    app = Flask(__name__)         #APP = FLASK INSTANCE THAT UTILIZES THE NAME OF OUR CURRENT MODULE
    # SETTING UP SOME CONFIGURATION THATS A DEFAULT
    app.config.from_mapping(      #WILL TAKE KEY WORD ARGUMENTS AND TURN THESE INTO SOME CONFIGURATION VALUES THAT WE HAVE ACCESS TO
        SECRET_KEY=os.environ.get("SECRET_KEY",default='dev')
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    return app
