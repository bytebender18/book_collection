from flask import Blueprint, render_template, jsonify, request
from repositories import book_repository
from repositories.book_repository import Book 

book_routes = Blueprint('book_routes',__name__)

@book_routes.route('/add',methods=['POST'])
def add_book():
	data = request.json
	author_id = data['author_id']
	book_name = data['book_name']
	year_published = data['year_published']
	genre = data['genre']
	book = book_repository.save_book_info(author_id, book_name, year_published, genre)

	return jsonify({'message':'Book Info saved successfully!!'})


@book_routes.route('/books/<string:name>',methods=['GET'])
def get_book_by_author_name(name):
	books = book_repository.fetch_book_by_author_name(name)
	response = []
	for book in books:
		response.append(book.to_json())
	return response
	if books is None:
		return None

@book_routes.route('/all/<string:name>',methods=['GET'])
def get_all_books(name):
	books = book_repository.fetch_all_books(name)
	response = []
	for book in books:
		response.append(book.to_json())
	return jsonify({'message':response})
	if books is None:
		return jsonify({"Error":"No book found"}),404
	return jsonify(response),200





