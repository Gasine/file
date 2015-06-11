from flask import Flask,render_template
import db
app = Flask(__name__)


@app.route('/')
def hello_world():
    categroy = db.sorted().getSort()
    article = db.blog().getallArticle()
    return render_template('list.html',categroy=categroy,article=article)
@app.route('/article/<int:id>')
def article(id):
    article = db.blog().getArticlebyid(id)

@app.route('/addarticle',methods=['POST'])
def addarticle():


if __name__ == '__main__':
    app.run()
