from flask_script import Manager
from blog import app
from blog.database import Entry, session,User
import os
from getpass import getpass
from werkzeug.security import generate_password_hash

manager = Manager(app)

@manager.command
def run():
    port = int(os.environ.get('PORT',8080))
    app.run(host='0.0.0.0',port=port)

@manager.command
def insert():
    content = """Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
    for i in range(25):
        entry = Entry(
            title = "Each Entry #{}".format(i),
            content = content
        )
        session.add(entry)
    session.commit()
    
@manager.command
def adduser():
    name = input("Name:")
    email = input("Email:")
    if session.query(User).filter_by(email=email).first():
        print("User with that email address already exists")
        return 
    
    password = ""
    password_2 = ""
    while len(password) < 8 or password !=password_2:
        password = getpass("Password:")
        password_2 = getpass("Re-enter password:")
    user = User(name=name,email=email,password=generate_password_hash(password))
    session.add(user)
    session.commit()

if __name__ == '__main__':
    manager.run()