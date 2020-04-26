from app import app, db
from app.models import *
import random as rs
from flask import jsonify, request


app.route('/')
def hello():
	return "hello"

@app.route('/serveAd')
def serveAd():
    ngosList = NGO.query.all()
    index = rs.randint(0,len(ngosList)-1)
    print(type(ngosList[index]))
    return jsonify((ngosList[index].as_dict()))

@app.route('/getNgoDetails')
def getNgoDetails():
    ngo = NGO.query.filter_by(id=request.args.get('ngoid')).first()
    pub = Publisher.query.filter_by(id=request.args.get('publisherid')).first()
    adlog = AdsLog(publisher_id=pub.id,ngo_id=ngo.id)
    db.session.add(adlog)
    db.session.commit()
    return jsonify((ngo.as_dict()))

@app.route('/getPublisherDetails')
def getPublisherDetails():
    pub = Publisher.query.filter_by(id=request.args.get('publisherid')).first()
    return jsonify((pub.as_dict()))

@app.route('/recordPayment')
def recordPayment():
    return "done"