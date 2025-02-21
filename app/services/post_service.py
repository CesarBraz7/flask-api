from app import db
from app.models.post import Post

def create_post(user_id, post=None,):
    if not post:
        return None

    new_post = Post(
        post = post,
        author_id = user_id
    )

    db.session.add(new_post)
    db.session.commit()

    return new_post

def get_post_by_id(id):
    return Post.query.get(id)

def get_posts():
    return Post.query.all()

def get_posts_by_user_id(user_id):
    return Post.query.filter_by(author_id=user_id).all()

def update_post(id, current_user, post_edit=None):
    post = Post.query.get(id)
    
    if not post:
        return None
    # verifica se o id do usuario atual é igual ao id do autor do post, verifica também se o usuario atual é um admin ou não
    if current_user.id != post.author_id and not current_user.is_admin:
        return "Unauthorized"

    if post_edit:
        post.post = post_edit

    db.session.commit()
    return post

def delete_post(id, current_user):
    post = Post.query.get(id)
    
    if not post:
        return None
    
    # verifica se o id do usuario atual é igual ao id do autor do post, verifica também se o usuario atual é um admin ou não
    if current_user.id != post.author_id and not current_user.is_admin:
        return "Unauthorized"

    db.session.delete(post)
    db.session.commit()

    return True