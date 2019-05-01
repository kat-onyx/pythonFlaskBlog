from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATSBASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.column(db.String(20), unique=True, nullable=False)
    username = db.column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        # print out
        return f"User('{self.username}', '{self.email}')"


@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html')

@app.route("/about")
def about():
    return "<h1>About Page</h1>"