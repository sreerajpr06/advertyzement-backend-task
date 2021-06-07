from operator import add
import os
from dotenv import load_dotenv
load_dotenv()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

database_uri = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 
db = SQLAlchemy(app)


class Banks(db.Model):
    name = db.Column(db.String())
    id = db.Column(db.Integer, primary_key=True)

    def __init__(self, name, id):
        super().__init__()
        self.name = name
        id = id

    def __repr__(self):
        return self.name


class Branches(db.Model):
    ifsc = db.Column(db.String())
    bank_id = db.Column(db.Integer, primary_key=True)
    branch = db.Column(db.String())
    address = db.Column(db.String())
    city = db.Column(db.String())
    district = db.Column(db.String())
    state = db.Column(db.String())

    def __init__(self, ifsc, bank_id, branch, address, city, district, state):
        super().__init__()
        self.ifsc = ifsc
        self.bank_id = bank_id
        self.branch = branch
        self.address = address
        self.city = city
        self.district = district
        self.state = state

    def __repr__(self):
        return self.ifsc


class BankBranches(db.Model):
    ifsc = db.Column(db.String())
    bank_id = db.Column(db.Integer, primary_key=True)
    branch = db.Column(db.String())
    address = db.Column(db.String())
    city = db.Column(db.String())
    district = db.Column(db.String())
    state = db.Column(db.String())
    bank_name = db.Column(db.String())

    def __init__(self, ifsc, bank_id, branch, address, city, district, state, bank_name):
        super().__init__()
        self.ifsc = ifsc
        self.bank_id = bank_id
        self.branch = branch
        self.address = address
        self.city = city
        self.district = district
        self.state = state
        self.bank_name = bank_name

    def __repr__(self):
        return self.ifsc


@app.route('/')
def index():
    return "Hello world"


@app.route('/banks')
def banks():
    banks = Banks.query.all()
    print(banks)
    return "hello"


@app.route('/branches')
def branches():
    branches = Branches.query.all()
    print(branches)
    return "branches"


@app.route('/bank_branches')
def bank_branches():
    bank_branches = BankBranches.query.all()
    print(bank_branches)
    return "bank_branches"


if __name__ == "__main__":
    app.run(debug = True)