import requests
from app.models import *
from random import choice

def find_matching_ad(ip):
    ngosList = NGO.query.filter_by(country=find_location(ip)).all()
    print(ngosList)
    if len(ngosList) == 0:
        ngosList = NGO.query.all()
    return choice(ngosList).as_dict()

def find_location(ip):
    try:
        response = requests.get("http://ip-api.com/json/{}".format(ip))
        js = response.json()
        print(js)
        country = js['countryCode']
    except:
        country = "IN"
    return country