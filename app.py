from flask import Flask, render_template, request, flash, redirect, session
from database.database import db, User
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'dialect://username:password@host:port/database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        repeat_password = request.form['repeatPassword']
        
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already registered!', 'error')
            return redirect('/register')

        if password != repeat_password:
            flash('Passwords do not match!', 'error')
            return redirect('/register')
        
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        
        flash('Successful Registration', 'success')
        return redirect('/login')
        
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        
        user = User.query.filter_by(email=email).first()
        
        if user and user.check_password(password):
            session['username'] = user.username
            flash('Login successful', 'success')
            return redirect('/')
        else:
            flash('Login failed. Check your credentials.', 'error')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out.', 'success')
    return redirect('/')

@app.route('/')
def home():
    return render_template('home.html', username=session.get('username'))

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
