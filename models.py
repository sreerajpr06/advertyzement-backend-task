from sqlalchemy import *
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship,
                            backref)
from sqlalchemy.ext.declarative import declarative_base

import os
from dotenv import load_dotenv
load_dotenv()

database_uri = os.environ.get('SQLALCHEMY_DATABASE_URI')
engine = create_engine(database_uri)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


# class Banks(Base):
#     __tablename__ = 'banks'
#     name = Column(String)
#     id = Column(Integer, primary_key=True)

#     def __init__(self, name, id):
#         super().__init__()
#         self.name = name
#         id = id

#     def __repr__(self):
#         return self.name


# class Branches(Base):
#     __tablename__ = 'branches'
#     ifsc = Column(String)
#     bank_id = Column(Integer, primary_key=True)
#     branch = Column(String)
#     address = Column(String)
#     city = Column(String)
#     district = Column(String)
#     state = Column(String)

#     def __init__(self, ifsc, bank_id, branch, address, city, district, state):
#         super().__init__()
#         self.ifsc = ifsc
#         self.bank_id = bank_id
#         self.branch = branch
#         self.address = address
#         self.city = city
#         self.district = district
#         self.state = state

#     def __repr__(self):
#         return self.ifsc


class BankBranches(Base):
    __tablename__ = 'bank_branches'
    ifsc = Column(String)
    bank_id = Column(Integer, primary_key=True)
    branch = Column(String)
    address = Column(String)
    city = Column(String)
    district = Column(String)
    state = Column(String)
    bank_name = Column(String)

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


with engine.connect() as connection:
    result = connection.execute("select * from banks")
    for row in result:
        print("Name: ", row['name'])