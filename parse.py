from config import *

import json
import requests

def postBook(book):
    headers = {
        'X-Parse-Application-Id': PARSE_APP_ID,
        'X-Parse-REST-API-Key': PARSE_API_KEY,
        'Content-Type': 'application/json'
    }

    r = requests.post('https://api.parse.com/1/classes/Book', headers=headers, data=json.dumps(book))

    return r

def getBookWithParams(params):
    headers = {
        'X-Parse-Application-Id': PARSE_APP_ID,
        'X-Parse-REST-API-Key': PARSE_API_KEY,
        'Content-Type': 'application/json'
    }

    r = requests.get('https://api.parse.com/1/classes/Book', headers=headers, params=params)

    return r.json()

def postCron(cron):
    headers = {
        'X-Parse-Application-Id': PARSE_APP_ID,
        'X-Parse-REST-API-Key': PARSE_API_KEY,
        'Content-Type': 'application/json'
    }

    r = requests.post('https://api.parse.com/1/classes/Cron', headers=headers, data=json.dumps(cron))

    return r
