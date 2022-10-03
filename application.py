from flask import Flask
from backend import create_app



if __name__ == "__main__":
    application = create_app()
    application.run(debug=True)

else:
    application = create_app()
