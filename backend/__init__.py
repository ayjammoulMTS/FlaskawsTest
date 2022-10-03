from flask import Flask
from Backend.testing2.summing import finals
from Backend.testing1.coins.eth  import eth
from Backend.testing2.summing  import test
from Backend.extensions         import extension



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
        return eth()

    app.register_blueprint(test)

    # app.run()

    return app


