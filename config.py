import os
from sqlalchemy import create_engine

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123@localhost/test_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# engine = create_engine('postgresql+psycopg2://postgres:123@hostname/test_db_1')
