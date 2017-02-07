import os
class DevelopmentConfig(object):
    SQLALCHEMY_DATABASE_URI = "postgresql://ubuntu:thinkful@localhost:5432/blogful"
    DEBUG = True
    SECRET_KEY = os.environ.get("\xf8mZ\xc5\xf47\xbe\xbc\xca\x84}\xa2",os.urandom(12))