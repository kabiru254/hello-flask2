import os


class Config(object):
    """Define app configuration"""
    SECRET_KEY= os.environ.get('SECRET_KEY') or 'hard to guess'
    