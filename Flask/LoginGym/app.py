from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_login import LoginManager, UserMixin, current_user, login_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@localhost/langganan_gym"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Anggota(db.Model):
    __tablename__ = "anggota"

    id: Mapped[int] = mapped_column(db.Integer, primary_key=True, autoincrement=True)
    nama: Mapped[str] = mapped_column(db.String(100), nullable=False)
    gender: Mapped[str] = mapped_column(db.String(100), nullable=True)
    ruangan: Mapped[str] = mapped_column(db.String(100), nullable=True)
    fitur: Mapped[str] = mapped_column(db.String(100), nullable=True)

# ------------ System Login ------------
app.config['SECRET_KEY'] = '3689c60d6d78663e65af191c5b88f400618d11e0a6df01b7120e723d4e8d'
login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin):
    def __init__(self,username,password):
        self.username = username
        self.password = password
    
    def get_id(self):
        return self.username
    
users = {
    'admin': User('admin','admin123'),
    'member': User('member','member123')
}
@login_manager.user_loader
def load_user(user_id):
    return users[user_id]

@login_manager.unauthorized_handler
def unauthorized():
    flash('ini perintah dari costum hanler. login dulu lah')
    return redirect(url_for('login'))

@app.context_processor
def inject_user():
    return {
        'user': current_user
    }

@app.route('/login', methods=['GET','POST'])
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
            flash('invalid credentials','error')

    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('profile'))


# ------------ System Login ------------
@app.get("/")
def index():
    anggota_list = Anggota.query.all()
    return render_template("index.html", anggota_list=anggota_list, user=current_user)

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route("/tambah", methods=["GET", "POST"])
def tambah():
    if request.method == "POST":
        nama = request.form["nama"]
        gender = request.form["gender"]
        ruangan = request.form["ruangan"]
        fitur = request.form["fitur"]
        
        anggota_baru = Anggota(nama=nama, gender=gender, ruangan=ruangan, fitur=fitur)
        db.session.add(anggota_baru)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("tambah.html")

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    anggota = Anggota.query.get(id)

    if request.method == "POST":
        anggota.nama = request.form["nama"]
        anggota.gender = request.form["gender"]
        anggota.ruangan = request.form["ruangan"]
        anggota.fitur = request.form["fitur"]
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("edit.html", anggota=anggota)

@app.get("/hapus/<int:id>")
def hapus(id):
    data = Anggota.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)




# flask shell
# from app import db
# db.create_all()
