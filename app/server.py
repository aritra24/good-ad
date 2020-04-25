from flask import Flask
from models import *

app = Flask(__name__)

@app.route('/')
def hello():
	return "Hello"


@app.route('/fetch')
def return_advert():
	return {"data":"we be returning stuff here"}


if __name__ == '__main__':
	app.run()