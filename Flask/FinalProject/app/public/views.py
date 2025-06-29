from flask import Blueprint, render_template, request
from flask_login import login_required
from app.post.models import Post, Category

blueprint = Blueprint("public", __name__, url_prefix="/")


@blueprint.route("/")
def home():
    category_filter = request.args.get("category")
    if category_filter:
        posts = Post.query.filter(Post.categories.any(id=category_filter)).order_by(Post.id.desc()).all()
    else:
        posts = Post.query.order_by(Post.id.desc()).all()
    categories = Category.query.all()
    return render_template("public/home.html", posts=posts, categories=categories)


@blueprint.get("/detail/<int:id>")
def detail(id):
    post = Post.query.get_or_404(id)
    return render_template("public/post.html", post=post)