from flask import Flask, render_template, request, redirect, session
import datetime
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from Request.request import Request
from dbUtils.dynamoUtils import DynamoUtils
from graphUtils.graphUtils import GraphUtils
from messageUtils.SqsUtils import SqsUtils
from messageUtils.SesUtils import SesUtils


application = Flask(__name__)
application.secret_key = "abc" 


@application.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@application.route('/login', methods=['POST', 'GET'])
def Login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        errMessage = 'Incorrect Credentials'
        scan = DynamoUtils.getItems('login')
        for item in scan:
            if request.form['email'] == item['user_email']['S'] and request.form['passwd'] == item['password']['S']:
                session['user_email'] = request.form['email']
                return redirect('/')

        return render_template('login.html', message=errMessage)


@application.route('/selection', methods=['POST'])
def processSelection():
    if request.method == 'POST':
        selection = request.form['submit_button']

        if selection == 'Awesome':
            return redirect('/Awesome')
        elif selection == 'Give':
            return redirect('/Give')
        elif selection == 'Morning':
            return redirect('/Morning')
        elif selection == 'Jinglebell':
            return redirect('/Jinglebell')
        elif selection == 'Ridiculous':
            return redirect('/Ridiculous')
        elif selection == 'Programmer':
            return redirect('/Programmer')
        elif selection == 'Graphs':
            return redirect('/graphs')


@application.route('/Awesome', methods=['POST', 'GET'])
def displayAwesome():
    if request.method == 'GET':
        requestUrl = Request.makeAwesomeUrl()
        text = Request.requestJson(requestUrl)
        args = {'Name': '',
                'Email':'',
                'Preview': text['response']}
        return render_template('Awesome.html', args=args)

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        reqType = request.form['submit_button']
        requestUrl = Request.makeAwesomeUrl(name)
        response = Request.requestJson(requestUrl)
        if reqType == 'Preview':
            args = {'Name': name,
                    'Email': email,
                    'Preview': response['response']}
            return render_template('Awesome.html', args=args)
        elif reqType == 'Send':
            message = response['response'] +'\n From: ' + session.get('user_email') + ',' + email

            DynamoUtils.updateItem('Awesome')
            SqsUtils.queueMessage(message)
            SesUtils.sendEmail()
            return redirect('/')

@application.route('/Give', methods=['POST', 'GET'])
def displayGive():
    if request.method == 'GET':
        requestUrl = Request.makeGiveUrl()
        text = Request.requestJson(requestUrl)
        args = {'Name': '',
                'Email':'',
                'Preview': text['response']}
        return render_template('Give.html', args=args)

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        reqType = request.form['submit_button']
        requestUrl = Request.makeGiveUrl(name)
        response = Request.requestJson(requestUrl)
        if reqType == 'Preview':
            args = {'Name': name,
                    'Email': email,
                    'Preview': response['response']}
            return render_template('Give.html', args=args)
        elif reqType == 'Send':
            message = response['response'] + ',' + email

            DynamoUtils.updateItem('Give')
            SqsUtils.queueMessage(message)
            SesUtils.sendEmail()
            return redirect('/')

@application.route('/Jinglebell', methods=['POST', 'GET'])
def displayJinglebell():
    if request.method == 'GET':
        requestUrl = Request.makeJingleUrl()
        text = Request.requestJson(requestUrl)
        args = {'Name': '',
                'Email':'',
                'Preview': text['response']}
        return render_template('Jinglebell.html', args=args)

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        reqType = request.form['submit_button']
        requestUrl = Request.makeJingleUrl(name)
        response = Request.requestJson(requestUrl)
        if reqType == 'Preview':
            args = {'Name': name,
                    'Email': email,
                    'Preview': response['response']}
            return render_template('Jinglebell.html', args=args)
        elif reqType == 'Send':
            message = response['response'] + ',' + email

            DynamoUtils.updateItem('Jinglebell')
            SqsUtils.queueMessage(message)
            SesUtils.sendEmail()
            return redirect('/')

@application.route('/Ridiculous', methods=['POST', 'GET'])
def displayRidiculous():
    if request.method == 'GET':
        requestUrl = Request.makeRidiculousUrl()
        text = Request.requestJson(requestUrl)
        args = {'Name': '',
                'Email':'',
                'Preview': text['response']}
        return render_template('Ridiculous.html', args=args)

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        reqType = request.form['submit_button']
        requestUrl = Request.makeRidiculousUrl(name)
        response = Request.requestJson(requestUrl)
        if reqType == 'Preview':
            args = {'Name': name,
                    'Email': email,
                    'Preview': response['response']}
            return render_template('Ridiculous.html', args=args)
        elif reqType == 'Send':
            message = response['response'] + ',' + email

            DynamoUtils.updateItem('Ridiculous')
            SqsUtils.queueMessage(message)
            SesUtils.sendEmail()
            return redirect('/')

@application.route('/Morning', methods=['POST', 'GET'])
def displayMorning():
    if request.method == 'GET':
        requestUrl = Request.makeMorningUrl()
        text = Request.requestJson(requestUrl)
        args = {'Name': '',
                'Email':'',
                'Preview': text['response']}
        return render_template('Morning.html', args=args)

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        reqType = request.form['submit_button']
        requestUrl = Request.makeMorningUrl(name)
        response = Request.requestJson(requestUrl)
        if reqType == 'Preview':
            args = {'Name': name,
                    'Email': email,
                    'Preview': response['response']}
            return render_template('Morning.html', args=args)
        elif reqType == 'Send':
            message = response['response'] + ',' + email

            DynamoUtils.updateItem('Morning')
            SqsUtils.queueMessage(message)
            SesUtils.sendEmail()
            return redirect('/')


@application.route('/Programmer', methods=['POST', 'GET'])
def displayProgrammer():
    if request.method == 'GET':
        requestUrl = Request.makeProgrammerUrl()
        text = Request.requestJson(requestUrl)
        args = {'Name': '',
                'Email':'',
                'Preview': text['response']}
        return render_template('Programmer.html', args=args)

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        reqType = request.form['submit_button']
        requestUrl = Request.makeProgrammerUrl(name)
        response = Request.requestJson(requestUrl)
        if reqType == 'Preview':
            args = {'Name': name,
                    'Email': email,
                    'Preview': response['response']}
            return render_template('Programmer.html', args=args)
        elif reqType == 'Send':
            message = response['response'] + ',' + email

            DynamoUtils.updateItem('Programmer')
            SqsUtils.queueMessage(message)
            SesUtils.sendEmail()
            return redirect('/')

@application.route('/Maybe', methods=['POST', 'GET'])
def displayM():
    if request.method == 'GET':
        requestUrl = Request.makeMaybeUrl()
        response = Request.requestJson(requestUrl)
        args = {'Name': '',
                'Preview': response['response']}
        return render_template('Maybe.html', args=args)

    if request.method == 'POST':
        name = request.form['name']
        requestUrl = Request.makeMaybeUrl(name)
        args = {'Name': name,
                'Preview': Request.requestText(requestUrl)}
        return render_template('Maybe.html', args=args)

@application.route('/LogAuth', methods=['POST'])
def authenticateCreds():
    errMessage = 'Incorrect Credentials'
    if request.method == 'POST':
        scan = DynamoUtils.getItems('login')
        for item in scan:
            if request.form['email'] == item['user_email']['S'] and request.form['passwd'] == item['password']['S']:
                return redirect('/')
        
        return redirect('login.html', message=errMessage)

@application.route('/graphs', methods=['POST', 'GET'])
def displayGraphs():
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
