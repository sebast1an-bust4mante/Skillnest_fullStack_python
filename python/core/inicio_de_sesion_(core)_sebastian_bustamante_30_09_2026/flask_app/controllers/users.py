from flask import render_template, request, redirect, url_for, session, flash
from flask_app import app
from flask_app.models.user import User
from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect('/dashboard')
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    if not User.validate_register(request.form):
        return redirect('/')

    hashed_password = generate_password_hash(request.form['password'])
    data = {
        "nombre": request.form['nombre'],
        "apellido": request.form['apellido'],
        "email": request.form['email'],
        "password": hashed_password
    }
    user_id = User.save(data)
    session['user_id'] = user_id
    return redirect('/dashboard')

@app.route('/login', methods=['POST'])
def login():
    user = User.get_by_email({'email': request.form['email']})
    if not user:
        flash("Correo o contraseña incorrectos.", "login")
        return redirect('/')

    if not check_password_hash(user.password, request.form['password']):
        flash("Correo o contraseña incorrectos.", "login")
        return redirect('/')

    session['user_id'] = user.id
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    
    user = User.get_by_id({'id': session['user_id']})
    return render_template('dashboard.html', user=user)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')