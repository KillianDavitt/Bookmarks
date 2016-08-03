from flask_login import login_user, logout_user, current_user, login_required, LoginManager
from datetime import datetime, timedelta, date
import time
from flask import render_template, flash, redirect, session, url_for, request
from app import app, db, lm
from .models import User, Bookmark

@app.route('/login', methods=["GET", "POST"])
def login():
    

    if request.method == "POST":
        
        password = request.form['password']

        if password != '':

            user = User.query.filter_by(name="killian").first()

            if password == user.password:
                #login
                login_user(user, remember=True)
                return redirect('/')

    return render_template('login.html')

@app.route('/bookmark_list', methods=['GET', 'POST'])
@app.route('/')
@login_required
def bookmark_list():
    
    bookmarks_list = None

    if request.method == 'POST':
        
        term = request.form['search']

        bookmark_list = Bookmark.query.filter(Bookmark.url.like("%" + term + "%")).all()

    else:
        bookmark_list = Bookmark.query.all()


    return render_template('bookmark_list.html', bookmark_list=bookmark_list)

@app.route('/bookmark/<anum>')
@login_required
def bookmark(anum):

    bookmark = Bookmark.query.filter_by(bookmark_id=anum).first()

    return render_template('bookmark.html', bookmark=bookmark)

@app.route('/new_bookmark', methods=['POST'])
@login_required
def new_bookmark():
    url = request.form['url']

    if url != "":
        
        new_bookmark = Bookmark(url=url)
        db.session.add(new_bookmark)
        db.session.commit()

    return redirect('/bookmark_list')

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@lm.unauthorized_handler
def unauthorized():
    return redirect(url_for('login'))

