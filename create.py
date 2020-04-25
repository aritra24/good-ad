from app import db
from app.models import *
db.create_all()
ngo1 = NGO(name="a_ngo")
pub1 = Publisher(name="a_publisher")
db.session.add(ngo1)
db.session.add(pub1)
db.session.commit()
