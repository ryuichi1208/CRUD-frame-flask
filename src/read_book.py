import json

def read_book_info(path):
    with open(path) as f:
        js = json.load(f)
        return js

