from flask import Flask, render_template, request
import sqlite3
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(500), nullable=False)
    email = db.Column(db.String(500), nullable=False)
    message = db.Column(db.Text, nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    messages = Messages.query.all()
    return render_template('index.html', messages=messages)


@app.route('/demo', methods=['GET', 'POST'])
def demo():
    return render_template('demo.html')



if __name__ == '__main__':
    app.run(debug=True)