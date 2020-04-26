from app import db
from datetime import datetime
from flask import json
import uuid

def generate_uuid():
    return str(uuid.uuid4())

class Publisher(db.Model):
    __tablename__ = "publisher"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=False)
    pub_since = db.Column(db.DateTime, default=datetime.utcnow)
    mobile = db.Column(db.Integer)
    email = db.Column(db.String(64))
    website = db.Column(db.String(64))
    about = db.Column(db.String(64))
    category = db.Column(db.String(164))
    ads_served = db.relationship('AdsLog',backref='publisher',lazy='dynamic')
    click_throughs = db.relationship('VisitedNGOLog', backref='publisher', lazy='dynamic')
    payments = db.relationship('PaymentInfo', backref='publisher_paid_to',lazy='dynamic')
    
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class NGO(db.Model):
    __tablename__ = "ngo"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=False)
    pub_since = db.Column(db.DateTime, default=datetime.utcnow)
    mobile = db.Column(db.Integer)
    email = db.Column(db.String(64))
    website = db.Column(db.String(64))
    about = db.Column(db.String(64))
    category = db.Column(db.String(164))
    country = db.Column(db.String(5))
    payments = db.relationship('PaymentInfo', backref='ngo_paid_to',lazy='dynamic')

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class PaymentInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(64))
    transaction_id = db.Column(db.String(64), default=generate_uuid,unique=True,nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    publisher_id = db.Column(db.Integer, db.ForeignKey('publisher.id'))
    amount = db.Column(db.Float, unique=False, nullable=False)
    ngo_id = db.Column(db.Integer, db.ForeignKey('ngo.id'))

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class AdsLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    publisher_id = db.Column(db.Integer, db.ForeignKey('publisher.id'))
    ngo_id = db.Column(db.Integer, db.ForeignKey('ngo.id'))

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class VisitedNGOLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    publisher_id = db.Column(db.Integer, db.ForeignKey('publisher.id'))
    ngo_id = db.Column(db.Integer, db.ForeignKey('ngo.id'))

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}



