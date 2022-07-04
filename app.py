from crypt import methods
from urllib import response
from flask import Flask, request, render_template, redirect, flash

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
    if num != len(responses):
        flash('please answer the questions in order', 'error')
        return redirect(f"/questions/{len(responses)}")

    
    elif num == len(questions):
        return redirect('/thankyou')
    else:
        return render_template('questions.html', questions=questions, num=num)

@app.route('/answer/<int:num>', methods=['POST'])
def test(num):
    if len(responses) < len(questions):
        option = request.form['options']
        responses.append(option)
        return redirect(f"/questions/{num}")
    else:
        return redirect('/thankyou')
    
@app.route('/thankyou')
def thank_you():
    return render_template('thankyou.html', responses=responses)