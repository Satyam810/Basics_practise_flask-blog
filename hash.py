from flask import Flask,request,redirect,render_template,flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///hash.db'
app.config['SECRET_KEY']='secret_key'
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(200),unique=True,nullable=False)
    password=db.Column(db.String(200),nullable=False)
with app.app_context():
    db.create_all()

@app.route('/login',methods=['GET','POST'])
def login

@app.route('/',methods=['GET','POST'])
def register():
    if request.method=='POST':
        username=request.form('username')
        password=request.form('password')
        if User.query.filter_by(username=username).first():
            flash("User already exists")
            return redirect('/')
        hashed_password=bcrypt.generate_password_hash(password).decode('utf-8')

        new_user=User(username=username,password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash("Registration successful!")
        return redirect('/')
    return render_template('index.html')

if __name__=='__main__':
    app.run()