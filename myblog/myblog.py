from flask import Flask,render_template,request,session,url_for,redirect
import db
import hashlib,json,re,base64
from datetime import datetime
app = Flask(__name__)

pagecount = 6

@app.route('/')
def hello_world():
    return redirect('/article/page/1')
@app.route('/Login')
def Login():
    return render_template('login.html')

@app.route('/login',methods=['POST'])
def login():
    user = request.form['user']
    password = request.form['password']
    if(hashlib.md5(password).hexdigest() == db.User().Validation(user)[0]):
        session['username'] = user
        return 'True'
    else:
        return 'False'

@app.route('/article/<int:id>')
def article(id):
    article = db.blog().getArticlebyid(id)
    categroy = db.sorted().getSort()
    if('username' in session):
        return render_template('article.html',username=session['username'],categroy=categroy,article=article)
    else:
        return render_template('article.html',categroy=categroy,article=article)

@app.route('/write')
def write():
    categroy = db.sorted().getSort()
    article = db.blog().getallArticle()
    return render_template('write.html',username=session['username'],categroy=categroy,article=article)

@app.route('/addarticle',methods=['POST'])
def addarticle():
    title = request.form['title']
    sortedValue = request.form['sorted']
    if( db.sorted().getSortid(sortedValue)):
        sortedValue = db.sorted().getSortid(sortedValue)
    else:
        return  'False'
    content = request.form['content']
    #content = content.replace('\n','<br/>')
    #content = content.replace(' ','&nbsp')
    date = request.form['date']
    if(not (title and sortedValue and content)):
        return 'False'
    if(db.blog().addArticle(title,session['username'],date,content,sortedValue)):
        return 'True'
    else:
        return 'False'

@app.route('/addcategory',methods=['GET'])
def addsort():
    arg = request.args
    sort = arg['sort']
    if(db.sorted().addSort(sort)):
        return 'True'
    else:
        return 'False'

@app.route('/getcategory')
def getcategory():
    category = db.sorted().getSort().all()
    a = {}
    b = 0
    for i in category:
        a[b] = i.name
        b += 1
    c=json.dumps(a)
    return c

@app.route('/delete/<int:id>',methods=['GET'])
def delete(id):
    if(db.blog().deleteArticle(id)):
        return "True"
    else:
        return "False"

@app.route('/update/<int:id>')
def update(id):
    categroy = db.sorted().getSort()
    article = db.blog().getArticlebyid(id)
    sort = db.sorted().getSortname(article.sorted).name
    return render_template('update.html',username=session['username'],categroy=categroy,article=article,sorted=sort)

@app.route('/updatearticle/<int:id>',methods=['POST'])
def updateAr(id):
    title = request.form['title']
    sortedValue = request.form['sorted']
    if( db.sorted().getSortid(sortedValue)):
        sortedValue = db.sorted().getSortid(sortedValue)
    else:
        return  'False'
    content = request.form['content']
    date = request.form['date']
    if(not (title and sortedValue and content)):
        return 'False'
    if(db.blog().updateArticle(id,title,date,content,sortedValue)):
        return 'True'
    else:
        return 'False'

@app.route('/sort/<int:id>')
@app.route('/sort/<int:id>/page/<int:num>')
def sort(id,num=1):
    sort = 'sort'
    categroy = db.sorted().getSort()
    count = db.blog().getCount(id)
    pagenum = (count/(pagecount+1))+1
    if (num==1):
        article = db.blog().getSortArticle(id).limit(pagecount).all()
    else:
        article = db.blog().getSortArticle(id).limit(pagecount).offset((num-1)*pagecount).all()

    x = min(6,pagenum + 1)
    y = min(pagenum + 1,num + 4)
    if('username' in session):
        return render_template('list.html',username=session['username'],categroy=categroy,article=article,count=pagenum,page=num,x=x,y=y,sort=sort,id=id)
    else:
        return render_template('list.html',categroy=categroy,article=article,count=pagenum,page=num,x=x,y=y,sort=sort,id=id)

@app.route('/article/page/<int:num>')
def pageNum(num):
    sort = 'article'
    pagecount = 6
    count = db.blog().getCount()
    pagenum = (count/(pagecount+1))+1
    categroy = db.sorted().getSort()
    if (num==1):
        article = db.blog().getallArticle().limit(pagecount).all()
    else:
        article = db.blog().getallArticle().limit(pagecount).offset((num-1)*pagecount).all()

    x = min(6,pagenum + 1)
    y = min(pagenum + 1,num + 4)
    if('username' in session):
        return render_template('list.html',username=session['username'],categroy=categroy,article=article,count=pagenum,page=num,x=x,y=y,sort=sort)
    else:
        return render_template('list.html',categroy=categroy,article=article,count=pagenum,page=num,x=x,y=y,sort=sort)

@app.route('/picture')
def showimg():
    return render_template('qiang.html')

@app.route('/getpic',methods=['POST'])
def getpic():
    pic = request.form['data']
    hz = request.form['houzui']
    now = datetime.now()
    name = now.strftime("%y-%m-%d %H:%M:%S") + '.' + hz
    pic = base64.decodestring(pic)
    with open('/home/gasine/git/myblog/static/img/pic/'+name,"wb") as f:
        f.write(pic)
    return 'True'

app.secret_key='\x02\x93r`3r\x81\xcf\x8bvx]<\xc2\xfc\xdb\x8c\xff\x8c)'


if __name__ == '__main__':
    app.run(port=8080,debug=True)

