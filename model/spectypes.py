from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from flask import session
import uuid
from api import db_session
from api import IAPI

from schemas import spectypes as s1
from .specmuts import specmut

Base = declarative_base()

class SpecType(Base):
    __tablename__ = 'g_spec_types'
    res_id = Column(String, primary_key=True)
    title = Column(String)
    descr = Column(String)
    pic = Column(String)
    dmp = s1.SSpecType()


    def getList(self):
        sess = db_session()
        m2 = list(sess.query(SpecType).order_by(SpecType.res_id.desc()).all())
        for id, item in enumerate(m2):
            m2[id].muts = specmut.get_specmuts_for_st(item.res_id)

        return self.dmp.dump(m2, many=True)

spectype = SpecType()

