from app import db
from app.models import *
from datetime import datetime
import uuid

db.create_all()
ngo1 = NGO(name="a_ngo",mobile=9999999999,email="email@ngo.com",website="www.ngowebsite.com",about="about ngo",category="ngo category",country="IN")
pub1 = Publisher(name="a_publisher",mobile=9999999991,email="email@pub.com",website="www.pubwebsite.com",about="about pub",category="pub category")
pub2 = Publisher(name="marthacooks",mobile=9873344813,email="martha@marthacooks.com",website="www.marthacooks.com",about="about martha",category="cooking")
payment1 = PaymentInfo(name="user1", email="email@1.com",amount=100)
payment1.publisher_paid_to=pub1
payment1.ngo_paid_to = ngo1
payment1.timestamp = datetime.now()
payment2 = PaymentInfo(name="user1", email="email@1.com",amount=25.5)
payment2.publisher_paid_to=pub1
payment2.ngo_paid_to = ngo1
payment2.timestamp = datetime.now()
db.session.add(ngo1)
db.session.add(pub1)
db.session.add(pub2)
db.session.add(payment1)
db.session.add(payment2)
db.session.commit()
