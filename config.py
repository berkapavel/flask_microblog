import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # configuration for forms
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'fNrW5HdfBXYyxRbSkfa7SCDENhywxxh9'
    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
