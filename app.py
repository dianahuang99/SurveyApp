from crypt import methods
from urllib import response
from flask import Flask, request, render_template, redirect, flash, session

import surveys

from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

debug = DebugToolbarExtension(app)

responses = []
questions = surveys.satisfaction_survey.questions

@app.route('/')
def show_home_page():
    title = surveys.satisfaction_survey.title
    instructions = surveys.satisfaction_survey.instructions
    return render_template('home.html', title=title, instructions=instructions)




@app.route('/questions/<int:num>')
def show_questions(num):
    if num != len(session['responses']):
        flash('please answer the questions in order', 'error')
        return redirect(f"/questions/{len(session['responses'])}")

    
    elif num == len(questions):
        return redirect('/thankyou')
    else:
        return render_template('questions.html', questions=questions, num=num)

@app.route('/answer/<int:num>', methods=['POST'])
def test(num):
    if len(session['responses']) < len(questions):
        option = request.form['options']
        responses = session['responses']
        responses.append(option)
        session['responses'] = responses
        return redirect(f"/questions/{len(session['responses'])}")
    else:
        return redirect('/thankyou')
    
@app.route('/thankyou')
def thank_you():
    return render_template('thankyou.html')


@app.route('/session', methods=["POST"])
def empty_responses():
    session['responses'] = []
    return redirect('/questions/0')
    