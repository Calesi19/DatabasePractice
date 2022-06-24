import pymongo
from pymongo import MongoClient
from pprint import pprint
import certifi

'''
ca = certifi.where()
cluster = MongoClient("mongodb+srv://Calesi19:Paola143@calesi.gn4hi.mongodb.net/?retryWrites=true&w=majority", tlsCAFile = ca)
db = cluster["sample_airbnb"]
collection = db["listingsAndReviews"]
post = {"_id": 0, "userName": "Calesi19", "score": 0}
collection.insert_one(post)
'''




def lookUpPlayer(userName):
    ca = certifi.where()
    cluster = MongoClient("mongodb+srv://Calesi19:Paola143@calesi.gn4hi.mongodb.net/?retryWrites=true&w=majority", tlsCAFile = ca)
    db = cluster["TypeSpace"]
    collection = db["playerScores"]
    return collection.find_one({"userName": userName})["score"]

score = lookUpPlayer("Calesi19")
print(score)