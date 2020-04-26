from app import app, db
from app.models import *
import random as rs
from flask import jsonify, request
from app.helpers import *

app.route('/')
def hello():
	return "hello"

@app.route('/serveAd')
def serveAd():
    publisher_id = request.args.get('publisherId')
    ngo = find_matching_ad(request.remote_addr)
    adsLog = AdsLog(timestamp=datetime.now(),publisher_id=publisher_id,ngo_id=ngo['id'])
    db.session.add(adsLog)
    db.session.commit()
    return jsonify(find_matching_ad(request.remote_addr))

@app.route('/getNgoDetails')
def getNgoDetails():
    ngo = NGO.query.filter_by(id=request.args.get('ngoId')).first()
    pub = Publisher.query.filter_by(id=request.args.get('publisherId')).first()
    admin = Publisher.query.filter_by(id=1).first()
    visitedNGOLog = VisitedNGOLog(publisher_id=pub.id,ngo_id=ngo.id)
    admin.total_due -= 0.01
    pub.total_due += 0.01
    db.session.commit()
    return jsonify((ngo.as_dict()))

@app.route('/getPublisherDetails')
def getPublisherDetails():
    pub = Publisher.query.filter_by(id=request.args.get('publisherId')).first()
    return jsonify((pub.as_dict()))

@app.route('/recordPayment',methods=['POST'])
def recordPayment():
    request_data = request.get_json()
    admin = Publisher.query.filter_by(id=1).first()
    ngo = NGO.query.filter_by(id=request_data['ngoId']).first()
    pub = Publisher.query.filter_by(id=request_data.get('publisherId')).first()
    paymentInfo = PaymentInfo(name=request_data.get('name'),email=request_data.get('email'),timestamp=datetime.now(),publisher_id=pub.id,ngo_id=ngo.id,amount=request_data.get('amount'))
    db.session.add(paymentInfo)
    db.session.commit()
    amount = request_data.get('amount')
    publisher_cut = 1
    ngo_cut = 0.95*amount
    infra = 0.05*amount - 1
    admin.total_due += infra
    ngo.total_due += ngo_cut
    pub.total_due += publisher_cut
    db.session.commit()
    return "Done"