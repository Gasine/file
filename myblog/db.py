#-*-coding:utf-8-*-
__author__ = 'gasine'
from config import *


from sqlalchemy import create_engine,Column,String,Integer,Text,desc,or_,and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql://{}:{}@localhost:3306/{}?charset=utf8'.format(db_username,db_password,db_db),pool_recycle=7200,encoding='utf-8',echo = False)
Session = sessionmaker(bind=engine)
dbsession = Session()
Base = declarative_base()


class blog(Base):
    __tablename__='blog'
    id = Column(Integer,primary_key=True)
    auth = Column(String(20))
    time = Column(String(20))
    title = Column(String(20))
    content = Column(Text)
    sorted = Column(Integer)

    def getSortArticle(self,sortedValue):
        return dbsession.query(blog).filter(blog.sorted == sortedValue).order_by(desc(blog.id))
    def addArticle(self,title,auth,time,content,sortedValue):
        article = blog(title=title, auth=auth, time=time, content=content, sorted=sortedValue)
        if (article):
            dbsession.add(article)
            dbsession.commit()
            return True
        else:
            return False
    def getallArticle(self):
        return dbsession.query(blog).order_by(desc(blog.id))
    def getArticlebyid(self,id):
        return dbsession.query(blog).filter(blog.id==id).first()
    def getCount(self,sortedValue =''):
        if (sortedValue ==''):
            return dbsession.query(blog).count()
        else :
            return dbsession.query(blog).filter(blog.sorted==sortedValue).count()
    def deleteArticle(self,id):
        article = dbsession.query(blog).filter(blog.id==id).first()
        if (article):
            dbsession.delete(article)
            dbsession.commit()
            return True
        else:
            return False
    def updateArticle(self,id, title, time,content,sorted):
        up = dbsession.query(blog).filter(blog.id==id)
        if(up):
            up.update({'title':title,'time':time,'content':content,'sorted':sorted})
            dbsession.commit()
            return True
        else:
            return False

class sorted(Base):
    __tablename__ = 'sorted'
    id = Column(Integer,primary_key=True)
    name = Column(String(20))

    def addSort(self,name):
        sort = sorted(name = name)
        if (sort):
            dbsession.add(sort)
            dbsession.commit()
            dbsession.close()
            return True
        else:
            return False

    def getSortid(self,name):
        sortedValue = dbsession.query(sorted).filter(sorted.name==name).first()
        if (sortedValue):
            return sortedValue.id
        else:
            return False
    def getSort(self):
        return dbsession.query(sorted)
    def getSortname(self,id):
        return dbsession.query(sorted).filter(sorted.id ==id).first()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True)
    username = Column(String(20))
    password = Column(String(20))
    def Validation(self,user):
        return dbsession.query(User.password).filter(User.username==user).first()

class picture(Base):
    __tablename__ = 'picture'
    id = Column(Integer,primary_key=True)
    name = Column(String(25))
    width = Column(Integer)
    height = Column(Integer)
    x = Column(Integer)
    y = Column(Integer)
    text = Column(Text)
    state = Column(Integer)
    onplay = Column(Integer)

    def getallpic(self):
        return dbsession.query(picture).order_by(desc(picture.id))
    def getonplay(self):
        return dbsession.query(picture).filter(picture.onplay==1).order_by(desc(picture.id))
    def updatestate(self,name,state):
        up = dbsession.query(picture).filter(picture.name==name)
        if(up):
            up.update({'state':state})
            return True
        else:
            return False
    def position(self,name,x,y):
        up = dbsession.query(picture).filter(picture.name==name)
        if(up):
            up.update({'x':x,'y':y})
            return True
        else:
            return False
    def addpic(self,name,width,height,x,y,state=1,onplay=0,text=''):
        pic = picture(name=name,width=width,height=height,x=x,y=y,text=text,state=state,onplay=onplay)
        if(pic):
            dbsession.add(pic)
            dbsession.commit()
            dbsession.close()
            return True
        else:
            return False