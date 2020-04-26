from app import app, db 
from app.models import *
import random as rs
from flask import jsonify, request, send_file
from app.helpers import *

@app.route('/')
def hello():
    return "hello"

@app.route('/serveAd/<publisher_id>')
def serveAd(publisher_id):
    ngo = find_matching_ad(request.remote_addr)
    adsLog = AdsLog(timestamp=datetime.now(),publisher_id=publisher_id,ngo_id=ngo['id'])
    db.session.add(adsLog)
    db.session.commit()
    return jsonify(find_matching_ad(request.remote_addr))

@app.route('/getNgoDetails')
def getNgoDetails():
    ngo = NGO.query.filter_by(id=request.args.get('ngoId')).first()
    pub = Publisher.query.filter_by(id=request.args.get('publisherId')).first()
    visitedNGOLog = VisitedNGOLog(publisher_id=pub.id,ngo_id=ngo.id)
    db.session.add(adlog)
    db.session.commit()
    return jsonify((ngo.as_dict()))

@app.route('/getPublisherDetails')
def getPublisherDetails():
    publisher_id = request.args.get('publisherId')
    pub = Publisher.query.filter_by(id=int(publisher_id)).first()
    return jsonify((pub.as_dict()))

@app.route('/recordPayment',methods=['POST'])
def recordPayment():
    request_data = request.get_json()
    ngo = NGO.query.filter_by(id=request_data['ngoId']).first()
    pub = Publisher.query.filter_by(id=request_data.get('publisherId')).first()
    print(ngo, pub, sep="\n")
    paymentInfo = PaymentInfo(name=request_data.get('name'),email=request_data.get('email'),timestamp=datetime.now(),publisher_id=pub.id,ngo_id=ngo.id,amount=request_data.get('amount'))
    db.session.add(paymentInfo)
    db.session.commit()
    return "Done"