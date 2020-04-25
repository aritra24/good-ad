from app import db
from datetime import datetime
from flask import json

def to_json(inst, cls):
    """
    Jsonify the sql alchemy query result.
    """
    convert = dict()
    # add your coversions for things like datetime's 
    # and what-not that aren't serializable.
    d = dict()
    for c in cls.__table__.columns:
        v = getattr(inst, c.name)
        if c.type in convert.keys() and v is not None:
            try:
                d[c.name] = convert[c.type](v)
            except:
                d[c.name] = "Error:  Failed to covert using ", str(convert[c.type])
        elif v is None:
            d[c.name] = str()
        else:
            d[c.name] = v
    return json.dumps(d)

class Publisher(db.Model):
    __tablename__ = "publisher"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=False)
    ads_served = db.relationship('AdsLog',backref='publisher',lazy='dynamic')
    click_throughs = db.relationship('VisitedNGOLog', backref='publisher', lazy='dynamic')
    payments = db.relationship('PaymentInfo', backref='publisher_paid_to',lazy='dynamic')

class NGO(db.Model):
    __tablename__ = "ngo"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=False)
    payments = db.relationship('PaymentInfo', backref='ngo_paid_to',lazy='dynamic')

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

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
