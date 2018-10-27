from models import Book

import firestore

### TESTING FIRESTORE ###

db = firestore.get_firestore_db('config/firestore-key.json')

book = Book(u'Frankenstein', u'2018-10-11', u'2018-10-27').to_dict()
print(book)

books_ref = db.collection(u'books')
books_ref.document(u'book').set(book)