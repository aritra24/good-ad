from app import db
from datetime import datetime

class Publisher(db.Model):
    __tablename__ = "publisher"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=False)
    ads_served = db.relationship('AdsLog',backref='publisher',lazy='dynamic')
    click_throughs = db.relationship('VisitedNGOLog', backref='publisher', lazy='dynamic')
    payments = db.relationship('PaymentInfo', backref='ngo',lazy='dynamic')

class NGO(db.Model):
    __tablename__ = "ngo"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=False)
    payments = db.relationship('PaymentInfo', backref='ngo',lazy='dynamic')

class PaymentInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=False)
    email = db.Column(db.String(64),unique=True)
    transaction_id = db.Column(db.String(64),unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    publisher_id = db.Column(db.Integer, db.ForeignKey('publisher.id'))
    ngo_id = db.Column(db.Integer, db.ForeignKey('ngo.id'))

class AdsLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    publisher_id = db.Column(db.Integer, db.ForeignKey('publisher.id'))
    ngo_id = db.Column(db.Integer, db.ForeignKey('ngo.id'))

class VisitedNGOLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    publisher_id = db.Column(db.Integer, db.ForeignKey('publisher.id'))
    ngo_id = db.Column(db.Integer, db.ForeignKey('ngo.id'))
