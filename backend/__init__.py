from flask import Flask
from backend.testing2.summing import finals
from backend.testing1.coins.eth  import Eth
from backend.testing2.summing  import test
from backend.extensions         import extension



def create_app():
    app = Flask(__name__)

    @app.route('/')
    def firstEnd():
        return ("Success Worked")

    @app.route('/nums')
    def stEnd():
        return finals()

    @app.route('/ext')
    def FRss():
        return extension()
    
    @app.route('/eth')
    def forreal():
        return Eth()

    app.register_blueprint(test)

    # app.run()

    return app


