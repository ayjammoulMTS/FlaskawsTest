from flask import Flask


application = Flask(__name__)

application.route('/')
def firstEnd():
    return ("Success Worked")
