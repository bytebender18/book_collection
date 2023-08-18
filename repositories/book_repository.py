from sqlalchemy import create_engine, Column, Integer, String, TIMESTAMP, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker
from repositories import author_repository
from repositories.author_repository import Author  


DATABASE_URL = 'postgresql://:@localhost/postgres'
engine = create_engine(DATABASE_URL)

metadata = MetaData()
metadata.reflect(engine)

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base(metadata=metadata)

class Book(Base):
	__tablename__ = 'books'

	def __init__(self, author_id, book_name, year_published, genre):
		self.author_id = author_id
		self.book_name = book_name
		self.year_published = year_published
		self.genre = genre

	def to_json(self):
		return {
		'id' : self.book_id,
		'author_id' : self.author_id,
		'book_name' : self.book_name,
		'year_published' : self.year_published,
		'genre' : self.genre
		}

Book.__table__ = Table('books', metadata, autoload=True, autoload_with=engine)

def save_book_info(author_id, book_name, year_published, genre):
	book = Book(author_id=author_id,book_name=book_name,year_published=year_published,genre=genre)
	session.add(book)
	session.commit()
	return book

def fetch_book_by_author_name(name):
	author = author_repository.fetch_author_by_name(name)
	book = session.query(Book).filter_by(book_name=name).all()
	return book 

def fetch_all_books(name):
	author = author_repository.fetch_author_by_name(name)
	books = session.query(Book).filter_by(author_id = author.author_id).all()
	return books
