from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from flask import session
import uuid
from api import db_session
from api import IAPI

from schemas import missions as s1
import smtplib

Base = declarative_base()

class Mission(Base):
    __tablename__ = 'g_missions'
    res_id = Column(String, primary_key=True)
    title = Column(String)
    description = Column(String)
    pic = Column(String)
    start_params = Column(String)
    start_specs = Column(String)

    dmp = s1.SMission()


    def getOne(self):
        sess = db_session()
        m2 = sess.query(Mission).first()
        return self.dmp.dump(m2)

mission = Mission()

