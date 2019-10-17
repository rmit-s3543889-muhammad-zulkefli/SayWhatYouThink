import boto3

class SqsUtils:

    sqs = boto3.client('sqs', region_name='us-west-2')

    @classmethod
    def queueMessage(cls, message):
        queues = cls.sqs.list_queues(QueueNamePrefix='Test')
        test_queue_url = queues['QueueUrls'][0]
        enqueue_response = cls.sqs.send_message(QueueUrl=test_queue_url, MessageBody=message)