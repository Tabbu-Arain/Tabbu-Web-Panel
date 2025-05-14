from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'your_default_secure_key')  # Use environment variable

# Default admin credentials (for testing; replace with database in production)
ADMIN_USERNAME = 'Tabbu-Arain'
ADMIN_PASSWORD = '7988U'

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Invalid credentials')
    return render_template('login.html')

@app.route('/index')
def index():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('index.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

# No app.run() needed for Render; handled by Gunicorn

if __name__ == '__main__':
    app.run()
