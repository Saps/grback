from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from flask import session
import uuid
from api import db_session
from api import IAPI

from schemas import specmuts as s1
import smtplib

Base = declarative_base()

class SpecMut(Base):
    __tablename__ = 'g_spec_muts'
    res_id = Column(String, primary_key=True)
    spec_type_id = Column(String)
    name = Column(String)
    descr = Column(String)
    pic = Column(String)
    price = Column(Float)

    dmp = s1.SSpecMut()


    def get_specmuts_for_st(self, st_id):
        result = db_session().query(SpecMut).filter(SpecMut.spec_type_id == st_id).all()
        return list(result)


specmut = SpecMut()

