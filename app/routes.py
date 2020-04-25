from app import app, db
from app.models import *
import random as rs
from flask import jsonify


app.route('/')
def hello():
	return "hello"

@app.route('/serveAd')
def serveAd():
    ngosList = []
    for i in range(1,11):
        ngosList.append({"name":"NGO"+str(i+1),"description":"NGO"+str(i+1)})
    index = rs.randint(0,len(ngosList)-1)
    return jsonify(ngosList[index])