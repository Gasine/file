#-*_coding:utf-8-*-
__author__ = 'gasine'
from config import *


from sqlalchemy import create_engine,Column,String,Integer,Text,desc,or_,and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql://{}:{}@localhost:3306/{}?charset=utf8'.format(db_username,db_password,db_db),pool_recycle=7200,encoding='utf-8',echo = False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class blog(Base):
    __tablename__='blog'
    id = Column(Integer,primary_key=True)
    auth = Column(String(20))
    time = Column(String(20))
    content = Column(Text)
    sorted = Column(Integer)

    def getSortArticle(self,sortedValue):
        return session.query(blog).filter(blog.sorted == sortedValue)
    def addArticle(self,auth,time,content,sortedValue):
        article = blog(auth = auth ,time = time,content = content,sorted=sortedValue)
        if (article):
            session.add(article)
            session.commit()
            return True
        else :
            return False
    def getallArticle(self):
        return session.query(blog)
    def getCount(self,sortedValue = ''):
        if (sorted !=''):
            return session.query(blog).count()
        else :
            return session.query(blog).filter(blog.sorted==sortedValue).count()
    def deleteArticle(self,id):
        pass
    def updateArticle(self):
        pass

class sorted(Base):
    __tablename__ = 'sorted'
    id = Column(Integer,primary_key=True)
    name = Column(String(20))

    def addSort(self,name):
        sort = sorted(name = name)
        session.add()
    def getSortid(self):
        pass
