""" Helper functions for using the Public Trello API.
"""

from config import *
import requests

def getMembersBoards(username, fieldArgs='all'):
    url = 'https://api.trello.com/1/members/%s/boards' % username
    params = {
        'fields': fieldArgs,
        'key': TRELLO_API_KEY
    }
    r = requests.get(url, params=params)

    return r.json()

def getListsInBoard(boardId, fieldArgs='all'):
    url = 'https://api.trello.com/1/boards/%s/lists' % boardId
    params = {
        'fields': fieldArgs,
        'key': TRELLO_API_KEY
    }
    r = requests.get(url, params=params)

    return r.json()

def getCardsInList(listId, actionArgs='all', fieldArgs='all'):
    url = 'https://api.trello.com/1/lists/%s/cards' % listId
    params = {
        'actions': actionArgs,
        'fields': fieldArgs,
        'key': TRELLO_API_KEY
    }
    r = requests.get(url, params=params)

    return r.json()

def findBoardInMembersBoardsByName(username, boardName):
    boards = getMembersBoards(username, fieldArgs='name')

    for board in boards:
        if board['name'] == boardName:
            return board['id']

def findListInBoardByName(boardId, listName):
    lists = getListsInBoard(boardId)

    for lst in lists:
        if lst['name'] == listName:
            return lst['id']
