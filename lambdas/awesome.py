import json
import os
import botocore
from botocore.vendored import requests
import boto3



def lambda_handler(event, context):
    
    url= "https://foaas.com/awesome"
    headers = {"Accept": "text/plain"}
    queryparam = ("/"+event.get('name'))
    response =  requests.get(url+queryparam,headers=headers)
    print(response.text)
    
    
    

    # TODO implement
    return {
        'response': response.text,
    }
