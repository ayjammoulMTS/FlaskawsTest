from backend.Testing1.adding import adding
from flask import Blueprint
from backend.testing2.tesitngalso import totest

def finals():
    return adding(4)


test = Blueprint("test", __name__, url_prefix="/test")

@test.get('/nothing')
def helloz():
    return adding(4)

@test.get('/ss')
def hellozss():
    return totest()

