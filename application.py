from flask import Flask
from backend.app import create_app


application = create_app()
# application.run()


# application = Flask(__name__)

# @application.route('/')
# def firstEnd():
#     return ("Success Worked")