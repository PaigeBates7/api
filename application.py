from flask import Flask

app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
bk = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.bk'

class Book(bk.Model):
    id = bk.Column(bk.Integer, primary_key=True)
    book_name =bk.Column(bk.str(80), unique=True, nullable=False)
    author = bk.Column(bk.str(120))
    publisher = bk.Column(bk.str(120))

    def __repr__(self):
        return f"{self.book_name} - {self.author} - {self.publisher}"

@app.route('/')
def index():
    return 'Hello'

@app.route('/Book')
def get_Book():
    book = Book.query.all()
    
    output = []
    for book in book:
      book_data = {'name': book_name, 'author': book.author}
      output.append(book_data)
    return {"Book": output}

@app.route('/book/<id>')
def get_book(id):
    book = book.query.get_or_404(id)
    return jsonify({"name":book.name, "author": book.author})

@app.route('/book', methods=['POST'])
def add_book():
    book = Book(name=request.json['name'], author=request.json['author'])
    bk.session.add(book)
    bk.session.commit()
    return {'id': book.id}

@app.route('/book/<id>', methods=['DELETE'])
def delete_book():
    book = Book.query.get(id)
    if book is None:
        return {"error": "not found"}
    bk.session.delete(book)
    bk.session.commit()
    return {"message": "yeet"}