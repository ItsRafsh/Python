# JUDUL: Authentication | No.3
# JUDUL: Authentication | No.5. lansung 5 di bagian def get_id()

from flask import Flask, request, render_template, flash, redirect, url_for
from flask_login import LoginManager, UserMixin, current_user, login_user, logout_user, login_required

app = Flask(__name__)

app.config['SECRET_KEY'] = '6d24379beae9d33333460cc11dbbdb5d5ef48d12e23aabd22d7793689f04406212e628'
login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin):
    def __init__(self,username,password):
        self.username = username
        self.password = password

    def get_id(self):
        return self.username

users = {
    'rafa': User(username='rafa', password='admin'),
    'haris': User(username='haris', password='admin2'),
}
@login_manager.user_loader
def load_user(user_id):
    return users[user_id]

# --- ini versi tidak kompleks
# login_manager.login_view = 'login'  # ini agar redirect disuruh login dari yg secret itu
# login_manager.login_message = 'login dulu lah baru ke rahasia'
# --- ini versi lebih kompleks
@login_manager.unauthorized_handler
def unauthorized():
    flash('ini perintah dari costum hanler. login dulu lah')
    return redirect(url_for('login'))


@app.context_processor
def inject_user():
    return {
        'user': current_user
    }

@app.get('/')
def index():
    return render_template('home.html')


@app.route(rule='/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = users.get(username)
        if not user:
            flash('user not found')
            return redirect(url_for('login'))

        if password == user.password:
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('invalid credentials')

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.get('/secret') #saat user ga login, lalu akses web ini ga bisa
@login_required     #karna ada fitur ini
def secret():
    return render_template('secret.html')



