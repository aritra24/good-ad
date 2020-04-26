from app import db
from app.models import *
from datetime import datetime
db.create_all()
ngo1 = NGO(name="a_ngo",mobile=9999999999,email="email@ngo.com",website="www.ngowebsite.com",about="about ngo",category="ngo category",country="IN")
pub1 = Publisher(name="a_publisher",mobile=9999999991,email="email@pub.com",website="www.pubwebsite.com",about="about pub",category="pub category")
payment1 = PaymentInfo(name="user1", email="email@1.com")
payment1.publisher_paid_to=pub1
payment1.ngo_paid_to = ngo1
payment1.timestamp = datetime.now()
db.session.add(ngo1)
db.session.add(pub1)
db.session.add(payment1)
db.session.commit()
