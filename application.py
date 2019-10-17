from flask import Flask, render_template, request, redirect, session
import random
import re
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from Request.request import Request
from dbUtils.dynamoUtils import DynamoUtils
from graphUtils.graphUtils import GraphUtils
from messageUtils.SqsUtils import SqsUtils
from messageUtils.SesUtils import SesUtils
from bucketUtils.bucketUtils import BucketUtils


application = Flask(__name__)
application.secret_key = "abc" 


@application.route('/', methods=['POST', 'GET'])
def index():
    if 'user_email' not in session:
        session['user_email'] = ''
        return redirect('/login')
    elif session['user_email']:
        return redirect('/home')
    else:
        return redirect('/login')

@application.route('/home', methods=['POST', 'GET'])
def home():
    if not session['user_email']:
        return redirect('/login')

    user = session['user_email']
    return render_template('Home.html', user= user)

@application.route('/login', methods=['POST', 'GET'])
def Login():
    if session['user_email']:
        return redirect('/home')

    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        errMessage = 'Incorrect Credentials'
        scan = DynamoUtils.getItems('login')
        for item in scan:
            if request.form['email'] == item['user_email']['S'] and request.form['passwd'] == item['password']['S']:
                session['user_email'] = request.form['email']
                return redirect('/')

        return render_template('index.html', message=errMessage)

@application.route('/Register', methods=['POST', 'GET'])
def Register():
    session['temp_email'], session['temp_passwd'] = '', ''
    if session['user_email']:
        return redirect('/home')

    if request.method == 'GET':
        return render_template('Register.html')
    if request.method == 'POST':
        errMessage = 'Email is in Incorrect format'
        emailReg = "^[^@\s]+@[^@\s]+\.[^@\s]+$"
        checkResult = re.search(emailReg, request.form['email'])
        if checkResult:
            scan = DynamoUtils.getItems('login')
            for item in scan:
                if request.form['email'] == item['user_email']['S']:
                    errMessage = "User already exists"
                    return render_template('Register.html', message=errMessage)

            session['temp_email'] = request.form['email']
            session['temp_passwd'] = request.form['passwd']
            allKeys = BucketUtils.getKeys()
            authKey = allKeys[random.randrange(15)]
            SesUtils.sendKey(authKey, request.form['email'])
            return redirect('/Authenticate')

        return render_template('Register.html', message=errMessage)

@application.route('/Authenticate', methods=['POST', 'GET'])
def displayAuth():
    if not session['temp_email']:
        return redirect('/login')


    if request.method == 'GET':
        return render_template('Authenticate.html')
    elif request.method == 'POST':
        errMessage = 'Incorrect Authentication Key'
        allKeys = BucketUtils.getKeys()
        for authKey in allKeys:
            if request.form['authKey'] == authKey:
                DynamoUtils.registerUser(session['temp_email'], session['temp_passwd'])
                session['user_email'] = session['temp_email']
                session['temp_email'], session['temp_passwd'] = '', ''
                return redirect('/home')

        return render_template('Authenticate.html', message=errMessage)


@application.route('/logout', methods=['POST', 'GET'])
def Logout():
    session['user_email'] = ''
    return redirect('/login')


@application.route('/Awesome', methods=['POST', 'GET'])
def displayAwesome():
    if not session['user_email']:
        return redirect('/login')

    destination = 'Awesome.html'

    if request.method == 'GET':
        requestUrl = Request.makeAwesomeUrl()
        return displayBasePage(requestUrl, destination)

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        reqType = request.form['submit_button']
        requestUrl = Request.makeAwesomeUrl(name)
        option = 'Awesome'
        return displayPreviewPage(
            name,email,reqType,requestUrl,destination, option)

@application.route('/Give', methods=['POST', 'GET'])
def displayGive():
    if not session['user_email']:
        return redirect('/login')

    destination = 'Give.html'

    if request.method == 'GET':
        requestUrl = Request.makeGiveUrl()
        return displayBasePage(requestUrl, destination)

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        reqType = request.form['submit_button']
        requestUrl = Request.makeGiveUrl(name)
        option = 'Give'
        return displayPreviewPage(
            name,email,reqType,requestUrl,destination, option)

@application.route('/Jinglebells', methods=['POST', 'GET'])
def displayJinglebell():
    if not session['user_email']:
        return redirect('/login')

    destination = 'Jinglebells.html'

    if request.method == 'GET':
        requestUrl = Request.makeJingleUrl()
        return displayBasePage(requestUrl, destination)

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        reqType = request.form['submit_button']
        requestUrl = Request.makeJingleUrl(name)
        option = 'Jinglebell'
        return displayPreviewPage(
            name,email,reqType,requestUrl,destination, option)

@application.route('/Ridiculous', methods=['POST', 'GET'])
def displayRidiculous():
    if not session['user_email']:
        return redirect('/login')

    destination = 'Ridiculous.html'

    if request.method == 'GET':
        requestUrl = Request.makeRidiculousUrl()
        return displayBasePage(requestUrl, destination)

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        reqType = request.form['submit_button']
        requestUrl = Request.makeRidiculousUrl(name)
        option = 'Ridiculous'
        return displayPreviewPage(
            name,email,reqType,requestUrl,destination, option)

@application.route('/Morning', methods=['POST', 'GET'])
def displayMorning():
    if not session['user_email']:
        return redirect('/login')

    destination = 'Morning.html'

    if request.method == 'GET':
        requestUrl = Request.makeMorningUrl()
        return displayBasePage(requestUrl, destination)

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        reqType = request.form['submit_button']
        requestUrl = Request.makeMorningUrl(name)
        option = 'Morning'
        return displayPreviewPage(
            name,email,reqType,requestUrl,destination, option)


@application.route('/Programmer', methods=['POST', 'GET'])
def displayProgrammer():
    if not session['user_email']:
        return redirect('/login')

    destination = 'Programmer.html'

    if request.method == 'GET':
        requestUrl = Request.makeProgrammerUrl()
        return displayBasePage(requestUrl, destination)

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        reqType = request.form['submit_button']
        requestUrl = Request.makeProgrammerUrl(name)
        option = 'Programmer'
        return displayPreviewPage(
            name,email,reqType,requestUrl,destination, option)

@application.route('/Cool', methods=['POST', 'GET'])
def displayCool():
    if not session['user_email']:
        return redirect('/login')

    destination = 'Cool.html'

    if request.method == 'GET':
        requestUrl = Request.makeCoolUrl()
        return displayBasePage(requestUrl, destination)

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        reqType = request.form['submit_button']
        requestUrl = Request.makeCoolUrl(name)
        option = 'Cool'
        return displayPreviewPage(
            name,email,reqType,requestUrl,destination, option)

@application.route('/Cup', methods=['POST', 'GET'])
def displayCup():
    if not session['user_email']:
        return redirect('/login')

    destination = 'Cup.html'

    if request.method == 'GET':
        requestUrl = Request.makeCupUrl()
        return displayBasePage(requestUrl, destination)

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        reqType = request.form['submit_button']
        requestUrl = Request.makeCupUrl(name)
        option = 'Cup'
        return displayPreviewPage(
            name,email,reqType,requestUrl,destination, option
            )

@application.route('/Diabetes', methods=['POST', 'GET'])
def displayDiabetes():
    if not session['user_email']:
        return redirect('/login')

    destination = 'Diabetes.html'

    if request.method == 'GET':
        requestUrl = Request.makeDiabetesUrl()
        return displayBasePage(requestUrl, destination)

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        reqType = request.form['submit_button']
        requestUrl = Request.makeDiabetesUrl(name)
        option = 'Diabetes'
        return displayPreviewPage(
            name,email,reqType,requestUrl,destination, option
            )

@application.route('/Fascinating', methods=['POST', 'GET'])
def displayFascinating():
    if not session['user_email']:
        return redirect('/login')

    destination = 'Fascinating.html'

    if request.method == 'GET':
        requestUrl = Request.makeFascinatingUrl()
        return displayBasePage(requestUrl, destination)

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        reqType = request.form['submit_button']
        requestUrl = Request.makeFascinatingUrl(name)
        option = 'Fascinating'
        return displayPreviewPage(
            name,email,reqType,requestUrl,destination, option
            )

@application.route('/Maybe', methods=['POST', 'GET'])
def displayMaybe():
    if not session['user_email']:
        return redirect('/login')

    destination = 'Maybe.html'

    if request.method == 'GET':
        requestUrl = Request.makeMaybeUrl()
        return displayBasePage(requestUrl, destination)

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        reqType = request.form['submit_button']
        requestUrl = Request.makeMaybeUrl(name)
        option = 'Maybe'
        return displayPreviewPage(
            name,email,reqType,requestUrl,destination, option
            )

@application.route('/Thanks', methods=['POST', 'GET'])
def displayThanks():
    if not session['user_email']:
        return redirect('/login')

    destination = 'Thanks.html'

    if request.method == 'GET':
        requestUrl = Request.makeThanksUrl()
        return displayBasePage(requestUrl, destination)

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        reqType = request.form['submit_button']
        requestUrl = Request.makeThanksUrl(name)
        option = 'Thanks'
        return displayPreviewPage(
            name,email,reqType,requestUrl,destination, option
            )

def displayBasePage(url, destination):
    text = Request.requestJson(url)
    args = {'Name': '',
            'Email':'',
            'Preview': text['response']}
    return render_template(destination, args=args)

def displayPreviewPage(name, email,reqType, url, destination, option):
    errMessage = ''
    response = Request.requestJson(url)

    emailReg = "^[^@\s]+@[^@\s]+\.[^@\s]+$"
    checkResult = re.search(emailReg, email)
    if not checkResult:
        errMessage = 'Incorrect Email Format'
        args = {'Name': name,
                'Email': email,
                'Preview': response['response']}
        return render_template(destination, args=args, errMessage=errMessage)

    if reqType == 'Preview':
        args = {'Name': name,
                'Email': email,
                'Preview': response['response']}
        return render_template(destination, args=args, errMessage=errMessage)
    elif reqType == 'Send':
        message = (response['response'] +
                    '\n From: '+
                    session['user_email']+
                    '*' + email)

        DynamoUtils.updateItem(option)
        SqsUtils.queueMessage(message)
        SesUtils.sendEmail(session['user_email'], email)
        return redirect('/')


@application.route('/Graphs', methods=['POST', 'GET'])
def displayGraphs():
    if not session['user_email']:
        return redirect('/login')

    if request.method == 'GET':
        scan = DynamoUtils.getItems()
        items = GraphUtils.makeGraphItems(scan)
        return render_template('graph.html', items=items, scan=scan)

    if request.method == 'POST':
        scan = DynamoUtils.getItems()
        items = GraphUtils.makeGraphItems(scan)
        return render_template('graph.html', items=items)


if __name__ == "__main__":
    application.run(debug=True)
