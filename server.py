from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from . spotify import spotify_get_current
from . spotify import send_spotify_command
from . auth import login_required
from . db import get_db

bp = Blueprint('script-server', __name__)

@bp.route('/', methods=('GET', 'POST'))
@login_required
def index():
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('blog/index.html', posts=posts)

@bp.route('/<username>', methods=('GET', 'POST'))
def user(username):
    '''Show User Info'''