from flask import Flask
from testProject.app import create_app


application = create_app()
application.run()


