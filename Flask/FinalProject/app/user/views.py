from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.user.models import User
from app.extensions import db, bcrypt
from flask_login import login_user, logout_user, login_required


blueprint = Blueprint('user', __name__, url_prefix='/user')

@blueprint.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('user/register.html')    

    username = request.form.get('username')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm-password')

    if password != confirm_password:
        flash(message='Password and confirm password not match',category='error')
        return render_template('user/register.html')


    user = User(username=username,password=bcrypt.generate_password_hash(password))
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('user.login'))



@blueprint.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('user/login.html')
    
    username = request.form.get('username')
    password = request.form.get('password')

    user = User.query.filter_by(username=username).first()
    if not user:
        flash(message='Username or password is invalid',category='error')
        return redirect(url_for('user.login'))

    if not bcrypt.check_password_hash(user.password, password):
        flash(message='Username or password is invalid',category='error')
        return redirect(url_for('user.login'))
    else:
        login_user(user)
        return redirect(url_for('public.home'))


@blueprint.route('/logout')
# @login_required()
def logout():
    logout_user()
    return redirect(url_for('public.home'))