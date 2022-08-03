
from flask import render_template, request, url_for, redirect, flash

from exams import bcrypt, db, app
from exams.forms import RegistrationForm, LoginForm, QuestionForm, QuizForm
from exams.models import Users, Question, Quiz
from flask_login import current_user, login_user, logout_user, login_required

# this is the home page
@app.route('/')
def home():
    return '<h1>Coming Soon</h1>'


# this route displays all the different quizzes that are available for the user to be able to pick his choice from
@app.route('/quiz')
def quiz_page():
    quizzes = Quiz.query.all()
    return render_template('quiz_page.html', quizzes=quizzes)

# register route
@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = Users(username=form.username.data,email=form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('You have been successfully registered','success')
        return redirect(url_for('login'))
    return render_template('register.html', form = form)

# login route
@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        user = Users.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            flash('Login was successful', 'success')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password','failure')
    return render_template('login.html', form = form)

# this route is for creating quizzes
@app.route('/quiz/new', methods=['GET','POST'])
def create_quiz():
    form = QuizForm()
    if form.validate_on_submit():
        quiz_info = Quiz(subject=form.subject.data,year=form.year.data, author = current_user)
        db.session.add(quiz_info)
        db.session.commit()
        flash('Quiz has been set. Set your questions now','info')
        return redirect(url_for('set_questions', quiz_id=quiz_info.id))
    return render_template('quiz.html', form=form)

# this route is for entering the questions into the data base
@app.route('/question/<int:quiz_id>',methods=['GET','POST'])
@login_required
def set_questions(quiz_id):
    form = QuestionForm()
    if form.validate_on_submit():
        questions = Question(question_text=form.question.data, answer_text=form.answers.data,quiz_id=quiz_id)
        db.session.add(questions)
        db.session.commit()
    return render_template('questionhub.html',form=form)


