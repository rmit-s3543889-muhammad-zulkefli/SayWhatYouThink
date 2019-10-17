import boto3
import json

class DynamoUtils:

    dynamodb = boto3.client('dynamodb', region_name='ap-southeast-2')
    choiceTable = 'choicesData'
    loginTable = 'login'

    @classmethod
    def getItems(cls, table=choiceTable):
        data = cls.dynamodb.scan(TableName=table)
        return data['Items']

    @classmethod
    def updateItem(cls, option):
        item = cls.dynamodb.get_item(TableName=cls.choiceTable, Key={'Option': {'S': option}})
        newTotal = int(item['Item']['Total']['N']) + 1
        cls.dynamodb.put_item(
            TableName = cls.choiceTable,
            Item = {
                    'Option': {'S': option},
                    'Total': {'N': str(newTotal)}
            }
        )

    @classmethod
    def registerUser(cls, email, passwd):
        cls.dynamodb.put_item(
            TableName = cls.loginTable,
            Item = {
                    'user_email': {'S': email},
                    'password': {'S': passwd}
            }
        )

