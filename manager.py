from getpass import getpass
from werkzeug.security import generate_password_hash
from blog.database import User

import os
from flask_script import Manager
from blog import app
from blog.database import Entry,session

manager = Manager(app)

@manager.command
def run():
    port = int(os.environ.get('PORT',8080))
    app.run(host='0.0.0.0',port=port)

@manager.command
def adduser():
    name = input("Name: ")
    email = input("Email: ")
    if session.query(User).filter_by(email=email).first():
        print("User with that email address already exists")
        return

    password = ""
    while len(password) < 8 or password != password_2:
        password = getpass("Password: ")
        password_2 = getpass("Re-enter password: ")
    user = User(name=name, email=email,password=generate_password_hash(password))
    session.add(user)
    session.commit()

if __name__ == '__main__':
    manager.run() 