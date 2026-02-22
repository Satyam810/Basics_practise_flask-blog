from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import datetime

# -------------------- APP CONFIG --------------------
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SECRET_KEY'] = 'secret_key'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# -------------------- EXTENSIONS --------------------
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# -------------------- MODELS --------------------

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)


# -------------------- CREATE DATABASE --------------------
with app.app_context():
    db.create_all()

# -------------------- BLOG ROUTES --------------------

@app.route('/')
def index():
    blogs = Blog.query.order_by(Blog.date_created.desc()).all()
    return render_template('index.html', blogs=blogs)


@app.route('/create', methods=['GET', 'POST'])
def create():
    if 'user' not in session:
        flash("Please login first")
        return redirect('/login')

    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        author = session['user']

        new_blog = Blog(title=title, description=description, author=author)
        db.session.add(new_blog)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('create.html')


@app.route('/blog/<int:id>')
def view(id):
    blog = Blog.query.get_or_404(id)
    return render_template('view.html', blog=blog)


# -------------------- AUTH ROUTES --------------------

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if User.query.filter_by(email=email).first():
            flash("User already exists")
            return redirect('/register')

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        new_user = User(email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful! Please login.")
        return redirect('/login')

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()

        if user and bcrypt.check_password_hash(user.password, password):
            session['user'] = user.email
            flash("Login successful!")
            return redirect('/')

        flash("Invalid credentials")

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('user', None)
    flash("Logged out successfully")
    return redirect('/')


# -------------------- RUN SERVER --------------------
if __name__ == "__main__":
    app.run(debug=True)