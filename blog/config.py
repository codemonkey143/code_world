import os
class DevelopmentConfig(object):
    SQLALCHEMY_DATABASE_URI = "postgresql://ubuntu:thinkful@localhost:5432/blogful"
    DEBUG  = True
    #need to set the secret key in order to block non authenticated people to edit blog
    SECRET_KEY = os.environ.get("BLOGFUL_SECRET_KEY",os.urandom(12))