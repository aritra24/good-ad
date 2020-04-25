from app import app, db
from app.models import *


app.route('/')
def hello():
	
	return "hello"