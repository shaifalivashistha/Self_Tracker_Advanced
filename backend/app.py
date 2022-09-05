from flask import Flask, render_template, request
from application.api import api
from application.models import db


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///livesess.sqlite3'
app.config['SECRET_KEY'] = 'secretkey'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api.init_app(app)
db.init_app(app)

@app.before_first_request
def database():
    db.create_all()


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    # if request.methods  == 'POST':
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)