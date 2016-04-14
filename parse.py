from config import *

import json
import requests

serverUrl = 'https://drejkim-reading-quantified.herokuapp.com/parse/'

def postBook(book):
    headers = {
        'X-Parse-Application-Id': PARSE_APP_ID,
        'X-Parse-REST-API-Key': PARSE_API_KEY,
        'Content-Type': 'application/json'
    }

    r = requests.post(serverUrl + 'classes/Book', headers=headers, data=json.dumps(book))

    return r

def getBooks(params=None):
    headers = {
        'X-Parse-Application-Id': PARSE_APP_ID,
        'X-Parse-REST-API-Key': PARSE_API_KEY,
        'Content-Type': 'application/json'
    }

    if params:
        r = requests.get(serverUrl + 'classes/Book', headers=headers, params=params)
    else:
        r = requests.get(serverUrl + 'classes/Book', headers=headers)

    return r.json()

def postCron(cron):
    headers = {
        'X-Parse-Application-Id': PARSE_APP_ID,
        'X-Parse-REST-API-Key': PARSE_API_KEY,
        'Content-Type': 'application/json'
    }

    r = requests.post(serverUrl + '/classes/Cron', headers=headers, data=json.dumps(cron))

    return r
