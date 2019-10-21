from botocore.vendored import requests



def lambda_handler(event, context):
    
    url= "https://foaas.com/cool"
    headers = {"Accept": "text/plain"}
    queryparam = ("/"+event.get('name'))
    response =  requests.get(url+queryparam,headers=headers)
    print(response.text)
    
    
    return {
        'response': response.text,
    }
