from flask import Flask, render_template
from author_routes import author_routes
from book_routes import book_routes


app = Flask(__name__)
app.register_blueprint(author_routes, url_prefix='/author')
app.register_blueprint(book_routes, url_prefix='/book')

if __name__ == '__main__':
	app.run(port=8080, debug= True)



