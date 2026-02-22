# from flask import Flask,render_template,request,redirect,flash
# from flask_sqlalchemy import SQLAlchemy
# from flask_bcrypt import Bcrypt
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# app.config['SECRET_KEY']='secret_key'
# db = SQLAlchemy(app)
# bcrypt=Bcrypt(app)

# class User(db.Model):
#     sno = db.Column(db.Integer,primary_key = True)
#     username = db.Column(db.String(200),unique=True,nullable = False)
#     password = db.Column(db.String(200),nullable = False)

# with app.app_context():
#     db.create_all()


# @app.route('/login',methods=['GET','POST'])
# def login():
#     if request.method=='POST':
#         username=request.form['username']
#         password=request.form['password']

#         user=User.query.filter_by(username=username).first()

#         if user and bcrypt.check_password_hash(user.password,password):
#             session['user']=user.username
#             return redirect('/')
#         flash("Invalid credentials")



# @app.route("/",methods = ['GET','POST'])
# def home():
#     if request.method == 'POST':
#         username = request.form["username"]
#         password = request.form["password"]
#         if User.query.filter_by(username=username).first():
#             flash("User already exists")
#             return redirect('/')
#         hashed_password=bcrypt.generate_password_hash(password).decode('utf-8')
#         new_user = User(username = username , password = hashed_password)
#         db.session.add(new_user)
#         db.session.commit()
    
#     users = User.query.all()
#     return render_template("index.html")
# # @app.route('/update',methods = ['GET','POST'])
# # def update():
# #     if request.method == 'POST':
# #         sno = request.form["sno"]
# #         username = request.form["username"]
# #         password = request.form["password"]
# #         user = User.query.filter_by(sno = sno).first()
# #         if user:
# #             user.username = username
# #             user.password = password
# #             db.session.add(user)
# #             db.session.commit()
# #     return render_template("update.html")

# if __name__ == "__main__":
#     app.run(debug = True)


# from flask import Flask, render_template, redirect, session, request, flash, url_for
# from flask_sqlalchemy import SQLAlchemy
# import base64

# app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user1.db'
# app.config['SECRET_KEY'] = 'secret_key'

# db = SQLAlchemy(app)

# # -------------------- MODEL --------------------
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(50), unique=True, nullable=False)
#     image = db.Column(db.LargeBinary, nullable=True)

# with app.app_context():
#     db.create_all()


# # -------------------- HOME --------------------
# @app.route('/', methods=['GET', 'POST'])
# def home():
#     if request.method == 'POST':
#         username = request.form['email']
#         image_file = request.files.get("image")  # ✅ Correct way

#         if User.query.filter_by(username=username).first():
#             flash("User already exists")
#             return redirect('/')

#         image_data = image_file.read() if image_file else None

#         new_user = User(
#             username=username,
#             image=image_data
#         )

#         db.session.add(new_user)
#         db.session.commit()

#         flash("User registered successfully")
#         return redirect('/')

#     return render_template("index.html")

# @app.route('/database')
# def database():
#     users = User.query.all()

#     for user in users:
#         if user.image:
#             user.image = base64.b64encode(user.image).decode('utf-8')
#         else:
#             user.image = None

#     return render_template("database.html", users=users)



# # -------------------- LOGOUT (optional) --------------------
# @app.route('/logout')
# def logout():
#     session.pop('user', None)
#     return redirect('/')


# if __name__ == "__main__":
#     app.run(debug=True)