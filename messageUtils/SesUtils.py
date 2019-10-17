import boto3

class SesUtils:

    sesClient = boto3.client('ses', region_name='us-west-2')
    sqs = boto3.client('sqs', region_name='us-west-2')
    defaultSender = "cloudcompass2@gmail.com"
    defaultRecipient = "yash.1996@hotmail.com"
    charset = "UTF-8"

    @classmethod
    def sendEmail(cls,sender, recipient):
        if not cls.compareVerifiedEmails(sender):
            sender = cls.defaultSender
        if not cls.compareVerifiedEmails(recipient):
            recipient = cls.defaultRecipient
        
        queues = cls.sqs.list_queues(QueueNamePrefix='Test')
        queue_url = queues['QueueUrls'][0]
        messages = cls.sqs.receive_message(QueueUrl=queue_url,MaxNumberOfMessages=1)

        sqsMessage = ''
        for message in messages['Messages']:
            sqsMessage = message['Body']
            cls.sqs.delete_message(QueueUrl=queue_url,ReceiptHandle=message['ReceiptHandle'])

        splitMessage = sqsMessage.split("*")
        bodyData = splitMessage[0]
        subject = ('To: ' + splitMessage[1])

        response = cls.sesClient.send_email(
            Destination={'ToAddresses':[recipient,],},
            Message={
                'Body':{
                    'Text': {
                        'Charset': cls.charset,
                        'Data': bodyData,
                    },
                },
                'Subject':{
                    'Charset': cls.charset,
                    'Data': subject,
                },
            },
            Source=sender,
        )
    
    @classmethod
    def sendKey(cls, authKey, email):

        if not cls.compareVerifiedEmails(email):
            email = cls.defaultSender

        bodyData = ('Your Authentication key is: ' + authKey)
        subject = ('SWYT Authentication Key for: ' + email)

        cls.sesClient.send_email(
            Destination={'ToAddresses':[email,],},
            Message={
                'Body':{
                    'Text': {
                        'Charset': cls.charset,
                        'Data': bodyData,
                    },
                },
                'Subject':{
                    'Charset': cls.charset,
                    'Data': subject,
                },
            },
            Source=cls.defaultSender,
        )
    
    @classmethod
    def compareVerifiedEmails(cls, refEmail):

        response = cls.sesClient.list_verified_email_addresses()
        for email in response['VerifiedEmailAddresses']:
            if refEmail == email:
                return True
        
        return False

