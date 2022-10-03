from backend.testing1.adding import adding
from flask import Blueprint

def finals():
    return adding(4)


test = Blueprint("test", __name__, url_prefix="/test")

@test.get('/nothing')
def helloz():
    return adding(4)
