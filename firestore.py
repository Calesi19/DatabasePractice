
class Firestore:
    def __init__(self):
        import firebase_admin
        from firebase_admin import credentials
        from firebase_admin import firestore
        self.__cred = credentials.Certificate("serviceAccountKey.json")
        firebase_admin.initialize_app(self.__cred)
        self.__db = firestore.client()
        self.__name = "Firestore"

    def getDatabaseName(self):
        return self.__name

    def createEntry(self, userName, score):
        self.__db.collection("playerScores").add({"name": userName, "score": score})

    def readEntries(self):
        for doc in self.__db.collection("playerScores").stream():
            username = doc.to_dict()["name"]
            score = doc.to_dict()["score"]
            print(f'\nUsername: {username}\nScore: {score}')

    def readEntry(self, userName):
        for doc in self.__db.collection("playerScores").where("name", "==", userName).stream():
            print(f'\nUsername: {username}\nScore: {score}')

    def updateEntry(self, userName, score):
        for doc in self.__db.collection("playerScores").where("name", "==", userName).stream():
            doc.reference.update({"score": score})

    def deleteEntry(self, userName):
        for doc in self.__db.collection("playerScores").where("name", "==", userName).stream():
            doc.reference.delete()

    def deleteAll(self):
        for doc in self.__db.collection("playerScores").stream():
            doc.reference.delete()

    def getEntries(self):
        entries = {}
        for doc in self.__db.collection("playerScores").stream():
            username = doc.to_dict()["name"]
            score = doc.to_dict()["score"]
            entries[username] = score
        return entries

    def populate(self, entries):
        for key in entries:
            self.createEntry(key, entries[key])


'''
firebase = Firestore()
firebase.createEntry("Calesi", 120)
firebase.readEntries()
firebase.updateEntry("Calesi", 100)
firebase.readEntries()
firebase.deleteAll()
firebase.readEntries()
dic = firebase.getEntries()
print(dic)
'''
