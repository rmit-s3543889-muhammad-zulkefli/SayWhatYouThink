from botocore.vendored import requests
import json


class Request:

    @staticmethod
    def makeAwesomeUrl(name='Anonymous'):
        if not name:
            name = 'Anonymous'
        url = 'https://a074imm2a8.execute-api.ap-southeast-2.amazonaws.com/Test?name=' + name
        return url

    @staticmethod
    def makeGiveUrl(name='Anonymous'):
        url = 'https://o396uduasf.execute-api.ap-southeast-2.amazonaws.com/give?name=' + name
        return url

    @staticmethod
    def makeJingleUrl(name='Anonymous'):
        url = 'https://6f849aittf.execute-api.ap-southeast-2.amazonaws.com/jinglebell?name=' + name
        return url

    @staticmethod
    def makeRidiculousUrl(name='Anonymous'):
        url = 'https://b3f8olowse.execute-api.ap-southeast-2.amazonaws.com/ridiculous?name=' + name
        return url

    @staticmethod
    def makeProgrammerUrl(name='Anonymous'):
        url = 'https://v32vx0fykc.execute-api.ap-southeast-2.amazonaws.com/programmer?name=' + name
        return url
    
    @staticmethod
    def makeMorningUrl(name='Anonymous'):
        url = 'https://v3ppfc5zs5.execute-api.ap-southeast-2.amazonaws.com/Morning?name=' + name
        return url
    
    @staticmethod
    def makeCoolUrl(name='Anonymous'):
        url = 'https://2yyj1bnlz1.execute-api.ap-southeast-2.amazonaws.com/Cool?name=' + name
        return url
    
    @staticmethod
    def makeCupUrl(name='Anonymous'):
        url = 'https://o6ddplah1k.execute-api.ap-southeast-2.amazonaws.com/Cup?name=' + name
        return url
    
    @staticmethod
    def makeDiabetesUrl(name='Anonymous'):
        url = 'https://m9jaaouv17.execute-api.ap-southeast-2.amazonaws.com/Diabetes?name=' + name
        return url
    
    @staticmethod
    def makeFascinatingUrl(name='Anonymous'):
        url = 'https://egppu65owd.execute-api.ap-southeast-2.amazonaws.com/Fascinating?name=' + name
        return url
    
    @staticmethod
    def makeMaybeUrl(name='Anonymous'):
        url = 'https://tzyocpgdmj.execute-api.ap-southeast-2.amazonaws.com/Maybe?name=' + name
        return url
    
    @staticmethod
    def makeThanksUrl(name='Anonymous'):
        url = 'https://77duvt4ko8.execute-api.ap-southeast-2.amazonaws.com/Thanks?name=' + name
        return url
    

    @staticmethod
    def requestJson(url):
        # contentType = {"Accept": "application/json"}
        r = requests.get(url)
        content = json.loads(r.text)
        return content

    @staticmethod
    def requestText(url):
        contentType = {"Accept": "text/plain"}
        r = requests.get(url, headers=contentType)
        return r.text
