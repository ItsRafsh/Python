from flask import redirect, flash
from werkzeug.exceptions import HTTPException

class InvalidCredentials(HTTPException):
    code = 401
    description = 'wrong username and password. please enter again!'

def handler_invalid_credentials(e: InvalidCredentials):
    flash(e.description, 'error coy')
    return redirect('/login')

class TooManyAttempt(HTTPException):
    code = 488
    description = 'Too Many Attempt. Try Again Later!!'
