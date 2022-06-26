
class MongoDatabase:
    def __init__(self):
        import pymongo
        from pymongo import MongoClient
        from pprint import pprint
        import certifi
        import constants
        self.__ca = certifi.where()
        self.__cluster = MongoClient(f"mongodb+srv://Calesi19:{constants.PASSWORD}@calesi.gn4hi.mongodb.net/?retryWrites=true&w=majority", tlsCAFile = self.__ca)
        self.__db = self.__cluster["TypeSpace"]
        self.__collection = self.__db["playerScores"]
        self.__name = "MongoDB"

    def getDatabaseName(self):
        return self.__name

    def createEntry(self, userName, score):
        self.__collection.insert_one({"userName": userName, "score": score})

    def readEntries(self):
        for entry in self.__collection.find():
            print(f'\nUsername: {entry["userName"]}\nScore: {entry["score"]}')

    def readEntry(self, userName):
        print(f'Username: {userName}\nScore: {self.__collection.find_one({"userName": userName})["score"]}')

    def updateEntry(self, userName, score):
        if self.__collection.find_one({"userName": userName})["score"] < score:
            myquery = {"userName": userName }
            newvalues = { "$set": { "score": score } }
            self.__collection.update_one(myquery, newvalues)

    def deleteEntry(self, userName):
        self.__collection.delete_many({"name": userName})

    def deleteAll(self):
        self.__collection.delete_many({})

    def getEntries(self):
        entries = {}
        for entry in self.__collection.find():
            username = entry["userName"]
            score = entry["score"]
            entries[username] = score
        return entries
    
    def populate(self, entries):
        for key in entries:
            self.createEntry(key, entries[key])

'''
mongo = MongoDatabase()
mongo.deleteAll()
mongo.createEntry("Calesi", 120)
mongo.readEntries()
mongo.updateEntry("Calesi", 300)
mongo.readEntries()
mongo.deleteAll()
mongo.readEntries()
dic = mongo.getEntries()
print(dic)
'''























'''
def isPlayerInDatabase(self, userName):
    exist_count = self.collection.find({"userName": userName}).count()
    if exist_count>=1:
        return True
    else:
        return False
'''