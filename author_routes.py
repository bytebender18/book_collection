from flask import Blueprint, render_template, jsonify, request
from repositories import author_repository
from repositories.author_repository import Author  


author_routes = Blueprint('author_routes',__name__)


@author_routes.route('/add',methods=["POST"])
def add_author():
	data = request.json 
	name = data['name']
	dob = data['dob']
	gender = data['gender']

	author_repository.save_author_info(name,dob,gender)

	return jsonify({'message':'Author Info saved successfully!!'}),200


@author_routes.route('/authors',methods=['GET'])
def get_authors():
	author = author_repository.fetch_all_authors()
	return jsonify({'Authors':author}),200


@author_routes.route('/authors/<string:name>',methods=['GET'])
def get_author_by_name(name):
	author = author_repository.fetch_author_by_name(name)
	return author.to_json()
