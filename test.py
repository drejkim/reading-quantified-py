from models import Book
from secret.trello_config import TRELLO_API_KEY
from trello import TrelloClient

import firestore

### TESTING py-trello ###

booksBoardId = 'mgqBN7ZV'

trelloClient = TrelloClient(api_key=TRELLO_API_KEY)
booksBoard = trelloClient.get_board(booksBoardId)

for listObject in booksBoard.list_lists():
    if listObject.name == 'Finished':
        finishedList = listObject.list_cards()

print(finishedList[0])

### TESTING FIRESTORE ###

# db = firestore.get_firestore_db('secret/firestore-key.json')

# book = Book(u'Frankenstein', u'2018-10-11', u'2018-10-27').to_dict()
# print(book)

# books_ref = db.collection(u'books')
# books_ref.document(u'book').set(book)