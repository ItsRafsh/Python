from flask import Flask, request, render_template, url_for,redirect
from typing import Optional, List


from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from flask_migrate import Migrate



app = Flask(__name__)
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres:postgres@localhost/myskill"
# initialize the app with the extension
db.init_app(app)
# initialize flask-migrate
migrate = Migrate()
migrate.init_app(app, db)

class User(db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    email: Mapped[str]
    phone: Mapped[Optional[str]]
    tasks: Mapped[List["Task"]] = relationship(back_populates="user")


class Task(db.Model):   
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    user_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="tasks")

    def __init__(self,name, user_id):
        self.name = name
        self.user_id = user_id


@app.route('/')
def home():
    tasks = Task.query.filter_by(user_id=1).all()
    return render_template(template_name_or_list='home.html', tasks=tasks)

@app.post('/tasks')
def create_task():
    task = Task(name=request.form['task'], user_id=1)
    db.session.add(task)
    db.session.commit()
    return redirect(url_for('home'))

@app.get('/tasks/<int:task_id>')
def edit_task(task_id):
    task = Task.query.get(task_id)
    return render_template(template_name_or_list='edit.html', task=task)

@app.post('/tasks/<int:task_id>')
def update_task(task_id):
    task = Task.query.get(task_id)
    task.name = request.form['task']
    db.session.commit()
    return redirect(url_for('home'))

@app.post('/tasks/<int:task_id>/delete')
def delete_task(task_id):
    task = Task.query.get(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('home'))




# with app.app_context():
# user = User()
# user.username = "rafa"
# user.email = 'rafa@myskill.id'
# db.session.add(user)
# db.session.commit()


