from django.db import models

# Create your models here.
from sqlalchemy import Column, String,Integer
from sqlalchemy.ext.declarative import declarative_base

Base  = declarative_base()

class myModel(Base):
    __tablename__ = 'login_creds'

    id=Column(Integer,primary_key=True)
    fname=Column(String(25))
    lname=Column(String(25))
    email=Column(String(25))
    pass1=Column(String(25))
    pass2=Column(String(25))
    phoneNum=Column(String(25))
    company=Column(String(25))