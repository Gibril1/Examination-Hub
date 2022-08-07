from exams import db, login_manager
from flask_login import UserMixin



@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.String(20), nullable = False)
    quizzes = db.relationship('Quiz', backref = 'author', lazy = True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return f'(Users({self.username},{self.email},{self.password})'

class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    subject = db.Column(db.String(30), nullable = False)
    year = db.Column(db.Integer, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    questions = db.relationship('Question', backref='quiz',lazy=True) 

    def __repr__(self):
        return f'Quiz({self.subject},{self.year})'

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.Text, nullable=False)
    answer_text =db.Column(db.Text, nullable = False)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)

    def __repr__(self):
        return f'Question({self.id},{self.question_text}, {self.answer_text}, {self.quiz_id})'    
    
    

   
    
    

    
    
