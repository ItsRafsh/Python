from flask import Flask, redirect, url_for, session, flash, get_flashed_messages, request
from .exceptions import InvalidCredentials,handler_invalid_credentials, TooManyAttempt

app = Flask(__name__)

app.register_error_handler(InvalidCredentials, handler_invalid_credentials)
app.secret_key = b'056249482ef931a61c394e4bf046c39c47217691f3a92f01fee387efa96fb13a' 

@app.get('/')
def index():
    # session.clear()       untuk membersihkan sisa login
    if 'username' in session:
        return f'Logged in as {session['username']}'
    return 'you are not logged in'

@app.get('/login')
def login_form():
    html = ''
    if len(get_flashed_messages())> 0:
        html += f'<h2>{get_flashed_messages()[0]}</h2>'

    html += '''
    <form action="/login" method="post">
        <label for="username">username: </label>
        <input type="text" id="username" name="username">
        <label for="password">password</label>
        <input type="password" id="password" name="password">
        <input type="submit">
    </form>
    '''
    return html

@app.post('/login')
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username == 'rafa' and password == 'admin':
        session['username'] = username
        session.pop(f'attempt_{username}', None)
        return redirect('/')
    else:
        session[f'attempt_{username}'] = session.get(f'attempt_{username}', 0) + 1
        print(session[f'attempt_{username}'])
        if session[f'attempt_{username}'] >= 3:
            raise TooManyAttempt
        raise InvalidCredentials
    

@app.get('/logout')
def logout():
    session.clear()
    return redirect('/')
