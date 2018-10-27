import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

def get_firestore_db(privateKeyJson):
    # Use a service account
    cred = credentials.Certificate(privateKeyJson)
    firebase_admin.initialize_app(cred)

    db = firestore.client()

    return db