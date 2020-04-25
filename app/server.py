from flask import Flask
from models import *
import random as rs
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def hello():
	return "Hello"


@app.route('/serveAd')
def serveAd():
    ngosList = []
    for i in range(1,11):
        ngosList.append({"name":"NGO"+str(i+1),"description":"NGO"+str(i+1)})
    index = rs.randint(0,len(ngosList)-1)
    return jsonify(ngosList[index])


if __name__ == '__main__':
	app.run()