from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import current_user, login_required
from app.post.models import Post, Category
from app.extensions import db


blueprint = Blueprint('post', __name__, url_prefix='/post')

@blueprint.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'GET':
        categories = Category.query.all()
        return render_template(template_name_or_list='post/create.html',categories=categories)

    else:
        title = request.form.get('title')
        body = request.form.get('body')
        categories = request.form.getlist('categories')

        post = Post(title=title, body=body, user_id=current_user.id)
        db.session.add(post)
        db.session.commit()

        categories = db.session.query(Category).filter(Category.id.in_(categories)).all()
        for category in categories:
            category.posts.append(post)
        db.session.commit()

        return render_template(template_name_or_list='post/create.html',categories=categories)

@blueprint.post('/delete/<int:id>')
@login_required
def delete(id):
    post = Post.query.get(id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('public.home'))

# @blueprint.route("/delete/<int:id>") ini gatau gagal
# @login_required
# def delete(id):
#     post = Post.query.filter(Post.id == id, Post.user_id == current_user.id).first()
#     if not post:
#         flash("Post not found", "error")
#         return redirect(url_for('public.home'))
#     db.session.delete(post)
#     db.session.commit()
#     return redirect(url_for('public.home'))