from html.parser import HTMLParser
from flask_restful import fields

class HTMLField(fields.Raw):

    def format(self, value):
        return strip_tags(str(value))

class HTMLStripper(HTMLParser):

    def __init__(self):
        self.reset()
        self.fed = []

    def handle_data(self, data):
        self.fed.append(data)

    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    stripper = HTMLStripper()
    stripper.feed(html)

    return stripper.get_data()
