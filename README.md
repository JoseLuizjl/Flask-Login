---

# Flask Login and Registration App

This is a basic web application built using Flask, SQLAlchemy, and Bcrypt to manage user registration and login. It supports user authentication, password hashing, and session management.

## Features

- **User Registration**: Users can create an account by providing a unique username, email, and password.
- **User Login**: Users can log in with their registered credentials.
- **Password Hashing**: User passwords are securely hashed using Bcrypt.
- **Session Management**: Once logged in, user sessions are maintained until they manually log out.
- **Flash Messages**: Informational messages are displayed to users after key actions (e.g., registration, login).
  
## Prerequisites

- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flask-Bcrypt
- MySQL (or compatible database)

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository
   ```

2. **Set up a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the Database**
   - Update `app.config['SQLALCHEMY_DATABASE_URI']` in `app.py` to point to your SQL database.

5. **Run the Application**
   ```bash
   python app.py
   ```

6. **Access the App**
   - Open your browser and go to `http://127.0.0.1:5000/`.

## How to Use

### Registration
- Go to `/register`, fill in the form with your username, email, and password. If successful, you'll be redirected to the home page.
  
### Login
- Go to `/login`, enter your username and password. After logging in, you’ll be redirected to the home page.

---
