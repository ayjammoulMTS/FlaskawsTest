from flask import Flask



def create_app():
    application = Flask(__name__)

    @application.route('/')
    def firstEnd():
        return ("Success Worked")

    return application
