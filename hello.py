import configparser
import time
import random
import os
import datetime
import ecapture as ec
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask import Flask, redirect, url_for, request, render_template
# from ecapture import ecapture as ec

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
blah = [], []
hey = 0
correct = 0
start = time.time()
done = time.time()
user = ""
configParser = configparser.ConfigParser()
configFilePath = r'config.py'
configParser.read(configFilePath)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        global blah
        global hey
        global correct
        global user
        blah = [], []
        hey = 0
        correct = 0
        user = request.form['nm']
        return redirect(url_for('welcome', name=user))
    else:
        return render_template('login.html')


@app.route('/question/<name>', methods=['POST', 'GET'])
@app.route('/welcome/<name>', methods=['POST', 'GET'])
def welcome(name):
    global blah
    global hey
    global correct
    global done
    global start

    if name == "admin":
        return redirect(url_for('admin'))

    if request.method == 'GET':
        return render_template('welcome.html', name=name, NumberOfQuestions=int(configParser.get('Config', 'NumberOfQuestions'))*len(configParser.get('Config', 'OperatorsTested')))

    if request.method == 'POST' and blah[0].__len__() == 0:
        blah = generate_questions_and_answers(int(configParser.get('Config', 'FirstAddLow')),
                                              int(configParser.get('Config', 'FirstAddHigh')),
                                              int(configParser.get('Config', 'SecondAddLow')),
                                              int(configParser.get('Config', 'SecondAddHigh')),
                                              int(configParser.get('Config', 'FirstSubtractLow')),
                                              int(configParser.get('Config', 'FirstSubtractHigh')),
                                              int(configParser.get('Config', 'SecondSubtractLow')),
                                              int(configParser.get('Config', 'SecondSubtractHigh')),
                                              int(configParser.get('Config', 'FirstMultiplyLow')),
                                              int(configParser.get('Config', 'FirstMultiplyHigh')),
                                              int(configParser.get('Config', 'SecondMultiplyLow')),
                                              int(configParser.get('Config', 'SecondMultiplyHigh')),
                                              int(configParser.get('Config', 'FirstDivideLow')),
                                              int(configParser.get('Config', 'FirstDivideHigh')),
                                              int(configParser.get('Config', 'SecondDivideLow')),
                                              int(configParser.get('Config', 'SecondDivideHigh')),
                                              configParser.get('Config', 'OperatorsTested'),
                                              str(int(configParser.get('Config', 'NumberOfQuestions')) + 1))
        form = LoginForm()
        form.question.label = str(blah[0][hey])
        return render_template('question.html', form=form, name=name)

    if request.method == 'POST':
        form = LoginForm()
        trier = request.form['nm']
        if trier == str(blah[1][hey]):
            hey = hey + 1
            correct = correct + 1
            if hey == blah[0].__len__():
                done = time.time()
                howlong = str(done-start)
                if float(howlong) > (len(configParser.get('Config', 'OperatorsTested'))*13)*int(configParser.get('Config', 'NumberOfQuestions')):
                    addtoleaderboard(howlong)
                    return render_template('done.html', form=form, name=name, howlong=howlong, correct=str(correct), hey=str(hey), message="Well Done - You drive a BMW", filename="level1.jpg")
                elif float(howlong) > (len(configParser.get('Config', 'OperatorsTested'))*12)*int(configParser.get('Config', 'NumberOfQuestions')):
                    addtoleaderboard(howlong)
                    return render_template('done.html', form=form, name=name, howlong=howlong, correct=str(correct), hey=str(hey), message="Well Done - You drive an Audi", filename="level2.jpg")
                elif float(howlong) > (len(configParser.get('Config', 'OperatorsTested'))*11)*int(configParser.get('Config', 'NumberOfQuestions')):
                    addtoleaderboard(howlong)
                    return render_template('done.html', form=form, name=name, howlong=howlong, correct=str(correct), hey=str(hey), message="Well Done - You drive a Lamborghini", filename="level3.jpg")
                elif float(howlong) > (len(configParser.get('Config', 'OperatorsTested'))*10)*int(configParser.get('Config', 'NumberOfQuestions')):
                    addtoleaderboard(howlong)
                    return render_template('done.html', form=form, name=name, howlong=howlong, correct=str(correct), hey=str(hey), message="Well Done - You drive a Lamborghini", filename="level4.jpg")
                else:
                    addtoleaderboard(howlong)
                    return render_template('done.html', form=form, name=name, howlong=howlong, correct=str(correct), hey=str(hey), message="Well Done - You Drive a Mclaren P1", filename="level5.jpg")
            form.question.label = str(blah[0][hey])
        else:
            form.question.label = str(blah[0][hey])
        return render_template('question.html', form=form, name=name)


@app.route('/admin', methods=['POST', 'GET'])
def admin():
    if request.method == 'GET':
        return render_template('admin.html', OperatorsTested=configParser.get('Config', 'OperatorsTested'),
                               NumberOfQuestions=configParser.get('Config', 'NumberOfQuestions'),
                               FirstAddLow=configParser.get('Config', 'FirstAddLow'),
                               FirstAddHigh=configParser.get('Config', 'FirstAddHigh'),
                               SecondAddLow=configParser.get('Config', 'SecondAddLow'),
                               SecondAddHigh=configParser.get('Config','SecondAddHigh'),
                               FirstSubtractLow=configParser.get('Config', 'FirstSubtractLow'),
                               FirstSubtractHigh=configParser.get('Config', 'FirstSubtractHigh'),
                               SecondSubtractLow=configParser.get('Config', 'SecondSubtractLow'),
                               SecondSubtractHigh=configParser.get('Config', 'SecondSubtractHigh'),
                               FirstMultiplyLow=configParser.get('Config', 'FirstMultiplyLow'),
                               FirstMultiplyHigh=configParser.get('Config', 'FirstMultiplyHigh'),
                               SecondMultiplyLow=configParser.get('Config', 'SecondMultiplyLow'),
                               SecondMultiplyHigh=configParser.get('Config', 'SecondMultiplyHigh'),
                               FirstDivideLow=configParser.get('Config', 'FirstDivideLow'),
                               FirstDivideHigh=configParser.get('Config', 'FirstDivideHigh'),
                               SecondDivideLow=configParser.get('Config', 'SecondDivideLow'),
                               SecondDivideHigh=configParser.get('Config', 'SecondDivideHigh'))
    if request.method == 'POST':
        configParser.set('Config', 'OperatorsTested', request.form['OperatorsTested'])
        configParser.set('Config', 'NumberOfQuestions', request.form['NumberOfQuestions'])
        configParser.set('Config', 'FirstAddLow', request.form['FirstAddLow'])
        configParser.set('Config', 'FirstAddHigh', request.form['FirstAddHigh'])
        configParser.set('Config', 'SecondAddLow', request.form['SecondAddLow'])
        configParser.set('Config', 'SecondAddHigh', request.form['SecondAddHigh'])
        configParser.set('Config', 'FirstSubtractLow', request.form['FirstSubtractLow'])
        configParser.set('Config', 'FirstSubtractHigh', request.form['FirstSubtractHigh'])
        configParser.set('Config', 'SecondSubtractLow', request.form['SecondSubtractLow'])
        configParser.set('Config', 'SecondSubtractHigh', request.form['SecondSubtractHigh'])
        configParser.set('Config', 'FirstMultiplyLow', request.form['FirstMultiplyLow'])
        configParser.set('Config', 'FirstMultiplyHigh', request.form['FirstMultiplyHigh'])
        configParser.set('Config', 'SecondMultiplyLow', request.form['SecondMultiplyLow'])
        configParser.set('Config', 'SecondMultiplyHigh', request.form['SecondMultiplyHigh'])
        configParser.set('Config', 'FirstDivideLow', request.form['FirstDivideLow'])
        configParser.set('Config', 'FirstDivideHigh', request.form['FirstDivideHigh'])
        configParser.set('Config', 'SecondDivideLow', request.form['SecondDivideLow'])
        configParser.set('Config', 'SecondDivideHigh', request.form['SecondDivideHigh'])
        with open('config.py', 'w') as configfile:
            configParser.write(configfile)
        return redirect(url_for('login'))


class LoginForm(FlaskForm):
    question = StringField('question', validators=[DataRequired()])
    submit = SubmitField('Enter')


def generate_questions_and_answers(add_1low, add_1high, add_2low, add_2high, sub_1low, sub_1high, sub_2low, sub_2high, mul_1low, mul_1high, mul_2low, mul_2high, div_1low, div_1high, div_2low, div_2high, operator, length):
    global start
    start = time.time()
    problem = []
    solution = []
    for x in range(1, int(length)):
        if "+" in operator:
            number_one = random.randrange(add_1low, add_1high)
            number_two = random.randrange(add_2low, add_2high)
            problem.append(str(number_one) + " + " + str(number_two))
            solution.append(number_one + number_two)
        if "-" in operator:
            number_one = random.randrange(sub_1low, sub_1high)
            number_two = random.randrange(sub_2low, sub_2high)
            problem.append(str(number_one) + " - " + str(number_two))
            solution.append(number_one - number_two)
        if "*" in operator:
            number_one = random.randrange(mul_1low, mul_1high)
            number_two = random.randrange(mul_2low, mul_2high)
            problem.append(str(number_one) + " x " + str(number_two))
            solution.append(number_one * number_two)
        if "/" in operator:
            number_one = random.randrange(div_1low, div_1high)
            if number_one == 0:
                number_one = number_one - 1
            number_two = random.randrange(div_2low, div_2high)
            divider = number_one * number_two
            problem.append(str(divider) + " / " + str(number_one))
            solution.append(divider // number_one)
    print(problem, solution)
    return problem, solution


def addtoleaderboard(howlong):
    date = str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    entry = '{"Name":"' + user + '","Date":"' + date + '","Time":"' + howlong + '"}'
    print(entry)
    entry = bytes(entry, 'utf-8')
    print(entry)
    with open('leaderboard.json', 'rb+') as f:
        f.seek(-3, os.SEEK_END)
        f.write(','.encode())
        f.write(entry)
        f.write(']'.encode())
        f.write('}'.encode())
        f.truncate()
    return


if __name__ == '__main__':
    app.run(debug=True)
