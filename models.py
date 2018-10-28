""" Data models
"""

class Book(object):
    def __init__(self, title, dateStarted, dateFinished):
        self.title = title
        self.dateStarted = dateStarted
        self.dateFinished = dateFinished

    def to_dict(self):
        dict = {
            u'title': self.title,
            u'dateStarted': self.dateStarted,
            u'dateFinished': self.dateFinished
        }

        return dict