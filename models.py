from db_connect import db
from datetime import datetime


class Post(db.Model):
    
    __tablename__ = 'post'

    def __init__(self,author,content):
        self.author = author
        self.content = content