from flask import Flask
from backend.testing2.summing import finals
from backend.testing2.summing  import test



def create_app():
    app = Flask(__name__)

    @app.route('/')
    def firstEnd():
        return ("Success Worked")

    @app.route('/nums')
    def stEnd():
        return finals()

    app.register_blueprint(test)

    # app.run()

    return app


