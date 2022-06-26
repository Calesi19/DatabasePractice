
class DynamoDB:
    def __init__(self):
        import boto3
        import requests
        import constants
        self.__client = boto3.client('dynamodb',aws_access_key_id=constants.AWSACCESSKEYID, aws_secret_access_key=constants.AWSSECRETKEY, region_name='us-west-1')
        self.__resource = boto3.resource('dynamodb',aws_access_key_id=constants.AWSACCESSKEYID, aws_secret_access_key=constants.AWSSECRETKEY, region_name='us-west-1')
        self.__table = self.__resource.Table('playerScores')
        self.__name = "DynamoDB"

        
    def getDatabaseName(self):
        return self.__name

    def createEntry(self, userName, score):
        item = { "username": {"S": userName},"score":{"N": f"{score}"}}
        self.__client.put_item(TableName="playerScores", Item=item)
    
    def readEntries(self):
        paginator = self.__client.get_paginator("scan")
        for page in paginator.paginate(TableName='playerScores'):
            for item in page["Items"]:
                score = int(item['score']['N'])
                userName = item['username']['S']
                print(f'\nUsername: {userName}\nScore: {score}')

    def readEntry(self, userName):
        response = self.__table.get_item(Key={'username': userName})
        print(f"\nUsername: {response['Item']['username']}\nScore: {response['Item']['score']}")


    def updateEntry(self, userName, score):
        item = { "username": {"S": userName},"score":{"N": f"{score}"}}
        self.__client.put_item(TableName="playerScores", Item=item)
    
    def deleteEntry(self, userName):
        response = table.delete_item(Key = {'username': userName})

    def deleteAll(self):
        tableKeyNames = [key.get("AttributeName") for key in self.__table.key_schema]

        #Only retrieve the keys for each item in the table (minimize data transfer)
        projectionExpression = ", ".join('#' + key for key in tableKeyNames)
        expressionAttrNames = {'#'+key: key for key in tableKeyNames}
        
        counter = 0
        page = self.__table.scan(ProjectionExpression=projectionExpression, ExpressionAttributeNames=expressionAttrNames)
        with self.__table.batch_writer() as batch:
            while page["Count"] > 0:
                counter += page["Count"]
                
                for itemKeys in page["Items"]:
                    batch.delete_item(Key=itemKeys)
                
                if 'LastEvaluatedKey' in page:
                    page = self.__table.scan(
                        ProjectionExpression=projectionExpression, ExpressionAttributeNames=expressionAttrNames,
                        ExclusiveStartKey=page['LastEvaluatedKey'])
                else:
                    break


    def getEntries(self):
        entries = {}
        paginator = self.__client.get_paginator("scan")
        for page in paginator.paginate(TableName='playerScores'):
            for item in page["Items"]:
                score = int(item['score']['N'])
                userName = item['username']['S']
                entries[userName] = score
        return entries

    def populate(self, entries):
        for key in entries:
            self.createEntry(key, entries[key])
        

'''
db = DynamoDB()
db.createEntry("tes45", 400)
db.readEntries()

dic = db.getEntries()
print(dic)
'''