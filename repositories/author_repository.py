from sqlalchemy import create_engine, Column, Integer, String, TIMESTAMP, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker


DATABASE_URL = 'postgresql://:@localhost/postgres'
engine = create_engine(DATABASE_URL)

metadata = MetaData()
metadata.reflect(engine)

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base(metadata=metadata)

class Author(Base):
	__tablename__ = 'author'

	def __init__(self,name,dob,gender):
		self.name = name 
		self.dob = dob
		self.gender = gender

	def to_json(self):
		return {
		'id':self.author_id,
		'name':self.name,
		'dob':self.dob,
		'gender':self.gender
		}

Author.__table__ = Table('author', metadata, autoload=True, autoload_with=engine)


def save_author_info(name,dob,gender):
	author = Author(name=name,dob=dob,gender=gender)
	session.add(author)
	session.commit()
	return author

def fetch_all_authors():
	authors = session.query(Author).all()
	response = []
	for author in authors:
		response.append(author.to_json())
	return response

def fetch_author_by_name(name):
	author = session.query(Author).filter_by(name=name).first()
	if author is None:
		return None
	return author





