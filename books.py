""" Functions for parsing Trello Books board and uploading books data to Parse.
"""

from pprint import pprint
import datetime
import dateutil.parser
import dateutil.tz
import parse
import trello

TRELLO_USERNAME = 'drejkim'
TRELLO_BOARD_NAME = 'Books'
TRELLO_LIST_TO_READ = 'To Read'
TRELLO_LIST_READING = 'Reading'
TRELLO_LIST_FINISHED = 'Finished'

def getCardsInFinishedList():
    boardId = trello.findBoardInMembersBoardsByName(TRELLO_USERNAME, TRELLO_BOARD_NAME)
    listId = trello.findListInBoardByName(boardId, TRELLO_LIST_FINISHED)
    cards = trello.getCardsInList(listId, actionArgs='updateCard')

    return cards

def getIsoDateForListChangeActions(action, listBeforeName, listAfterName):
    if 'listBefore' not in action['data']:
        return

    listBefore = action['data']['listBefore']['name']
    listAfter = action['data']['listAfter']['name']

    if listBefore == listBeforeName and listAfter == listAfterName:
        return action['date']

def createBook(card):
    book = {
        'title': card['name'],
        'cardId': card['id'],
        'dateStarted': None,
        'dateFinished': None,
        'daysToFinish': None,
    }
    dateStarted = None
    dateFinished = None

    if card['actions']:
        actions = card['actions']

        for action in actions:
            isoDateStarted = getIsoDateForListChangeActions(action, TRELLO_LIST_TO_READ, TRELLO_LIST_READING)
            if isoDateStarted:
                dateStarted = dateutil.parser.parse(isoDateStarted)
                book['dateStarted'] = {
                    '__type': 'Date',
                    'iso': isoDateStarted
                }

            isoDateFinished = getIsoDateForListChangeActions(action, TRELLO_LIST_READING, TRELLO_LIST_FINISHED)
            if isoDateFinished:
                dateFinished = dateutil.parser.parse(isoDateFinished)
                book['dateFinished'] = {
                    '__type': 'Date',
                    'iso': isoDateFinished
                }

        if dateStarted and dateFinished:
            book['daysToFinish'] = (dateFinished.date() - dateStarted.date()).days

            if card['labels']:
                labels = card['labels']
                categories = []
                for label in labels:
                    categories.append(label['name'])

                book['categories'] = categories

            return book
        else:
            return None
    else:
        return None

def main():
    print 'Get books in Parse...'
    booksInParse = parse.getBooks()['results']
    existingCardIds = [book['cardId'] for book in booksInParse]
    print 'Done.'

    print 'Get cards from Trello...'
    cards = getCardsInFinishedList()
    print 'Done.'

    for card in cards:
        if card['id'] not in existingCardIds:
            book = createBook(card)
            if book:
                print 'Uploading to Parse...'
                r = parse.postBook(book)

                pprint(book)
                print r

    now = datetime.datetime.now(dateutil.tz.tzutc())
    cron = {
        'ranAt': {
            '__type': 'Date',
            'iso': now.isoformat()
        }
    }
    r = parse.postCron(cron)
    pprint(cron)
    print r

if __name__ == '__main__':
    main()
