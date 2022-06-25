

class Director:
    def __init__(self):
        import mongodb
        import firestore
        import dynamodb
        import os
        import time
        self.clear = lambda: os.system('cls')
        self.__firestoreDB = firestore.Firestore()
        self.__mongoDB = mongodb.MongoDatabase()
        self.__dynamoDB = dynamodb.DynamoDB()
        self.__databases = [self.__firestoreDB, self.__mongoDB, self.__dynamoDB] 


    def main(self):

        while True:
            choice = None
            print(f"\nSelect one of the following options:\n1.Create New Entry\n2.Read all entries\n3.Update Entry\n4.Delete Entry\n5.Delete All Entries")
            while choice not in ["1", "2", "3", "4", "5"]:
                choice = (input("\nEnter a number choice >"))

            choice = int(choice)
            dbchoice = None
            print(f"\nWhich database would you wish to choose:\n1.Firestore\n2.MongoDB\n3.DynamoDB")
            while dbchoice not in ["1", "2", "3"]:
                dbchoice = input("\nEnter a number choice >")

            database = self.__databases[int(dbchoice) - 1]

            if choice == 1:
                self.clear()
                print(f"\nCreating new entry in {database.getDatabaseName()}:")
                userName = input("Enter the player's username: ")
                score = int(input("Enter the player's score:")) 
                database.createEntry(userName, score)
                self.clear()
                print("[RECORDED]")
                

            elif choice == 2:
                database.readEntries()
                proceed = input("......continue")
                self.clear()

            elif choice == 3:
                self.clear()
                print(f"\nUpdating entry in {database.getDatabaseName()}:")
                userName = input("Enter the player's username: ")
                score = int(input("Enter the player's score:")) 
                database.updateEntry(userName, score)
                self.clear()
                print("[UPDATED]")
            

            elif choice == 4:
                self.clear()
                print(f"\nDeleting entry in {database.getDatabaseName()}:")
                userName = input("Enter the player's username: ")
                database.deleteEntry(userName)
                self.clear()
                print("[DELETED]")
            

            elif choice == 5:
                database.deleteAll()
                self.clear()
                print("[DATABASE CLEARED]")

        
        
