from flask import Flask, request, render_template, redirect, flash

import surveys

from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

debug = DebugToolbarExtension(app)

responses = []

@app.route('/')
def show_home_page():
    title = surveys.satisfaction_survey.title
    instructions = surveys.satisfaction_survey.instructions
    return render_template('home.html', title=title, instructions=instructions)




@app.route('/questions/<int:num>')
def show_questions(num):
    questions = surveys.satisfaction_survey.questions
    # questions_length = len(questions) -1
    return render_template('questions.html', questions=questions, num=num)