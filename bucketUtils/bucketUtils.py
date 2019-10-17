import boto3
import json

class BucketUtils:

    s3 = boto3.resource('s3')
    bucket = s3.Bucket('cloudcompass2-yash-adib')
    obj = bucket.Object('authKey.json')

    @classmethod
    def getKeys(cls):
        body = cls.obj.get()['Body'].read().decode("utf-8")
        keys = json.loads(body)
        return keys['keys']

