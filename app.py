from flask import Flask



def create_app():
    app = Flask(__name__)

    @app.route('/')
    def firstEnd():
        return ("Success Worked")

    app.run()

    return app


