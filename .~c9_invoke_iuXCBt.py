import os
from flask_script import Manager
from blog import app

from blog.database import Entry,session

manager = Manager(app)

@manager.command
def run():
    port = int(os.environ.get('PORT',8080))
    app.run(host='0.0.0.0',port=port)
    
'''
@manager.command
def seed():
    content = """Adobe Systems Incorporated doʊbi is an American multinational computer software company.The company is headquartered in San Jose, California, United States. Adobe has historically focused upon the creation of multimedia and creativity software products, with a more recent foray towards rich Internet application software development. It is best known for Photoshop, an image editing software, Acrobat Reader, the Portable Document Format (PDF) and Adobe Creative Suite, as well as its successor Adobe Creative Cloud"""
    for i in range(25):
        entry = Entry(
            title = "Test Entry #{}".format(i),
            content = content
        )
        session.add(entry)
    session.commit()
    
'''

@

if __name__ == '__main__':
    manager.run() 