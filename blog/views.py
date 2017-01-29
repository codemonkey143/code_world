from flask import render_template
from . import app
from .database import session,Entry
from flask import request, redirect, url_for
from .database import User
from flask import flash
from flask_login import LoginManager,login_required,login_user
from werkzeug.security import check_password_hash

PAGINATE_BY = 10

@app.route("/")
@app.route("/page/<int:page>")
def entries(page=1):
    # Zero-indexed page
    page_index = page - 1

    count = session.query(Entry).count()

    start = page_index * PAGINATE_BY
    end = start + PAGINATE_BY

    total_pages = (count - 1) // PAGINATE_BY + 1
    has_next = page_index < total_pages - 1
    has_prev = page_index > 0

    entries = session.query(Entry)
    
    entries = entries.order_by(Entry.datetime.desc())
    entries = entries[start:end]
    return render_template("entries.html",
        entries=entries,
        has_next=has_next,
        has_prev=has_prev,
        page=page,
        total_pages=total_pages
    )

# It display the page you entered
@app.route("/entry/<int:page>")
def entries_page(page):
    page = page + 1
    entries = session.query(Entry)
    entries = entries.filter_by(id=page)
    return render_template("entries.html",entries=entries)
    
@app.route("/entry/<int:page>/edit", methods=["GET"])
def entries_edit_get(page):
    page = page
 
    entries = session.query(Entry.title,Entry.content).filter_by(id=page)
    for entry in entries:
        title = entry.title
        content = entry.content
    return render_template("entries_edit.html",title=title,content=content)

from sqlalchemy import update
@app.route("/entry/<int:page>/edit", methods=["POST"])
def entries_edit_post(page):
    page = page 
    #session.query(Entry).filter(Entry.id==page).update(Entry.title=entry.title,Entry.content=entry.content)
    #session.query(Entry).filter(Entry.id==page).update({"Entry.title":request.form["title"]},{"Entry.content":request.form["content"]})
    admin = session.query(Entry).filter_by(id=page).first()
    admin.title = request.form["title"]
    admin.content = request.form["content"]

    session.commit()
    return redirect(url_for("entries"))
    

@app.route("/entry/add", methods=["GET"])
def add_entry_get():
    return render_template("add_entry.html")

@app.route("/entry/add", methods=["POST"])
@login_required
def add_entry_post():
    entry = Entry(
        title=request.form["title"],
        content=request.form["content"],
    )
    session.add(entry)
    session.commit()
    return redirect(url_for("entries"))
    
@app.route("/login",methods=["GET"])
def login_get():
    return render_template("login.html")

@app.route("/login",methods=["POST"])
def login_post():
    email = request.form["email"],
    password = request.form["password"]
    user = session.query(User).filter_by(email=email).first()
    if not user or not check_password_hash(user.password,password):
        flash("incorrect username or password","danger")
        return redirect(url_for("login_get"))
    
    login_user(user)
    return redirect(request.args.get('next') or url_for("entries"))