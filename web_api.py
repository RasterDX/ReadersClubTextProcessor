import requests


URL = "https://readers-club-api.herokuapp.com/"
add_book = "books/add"
add_loc = ""

def persist_locations(location_map):
    r = requests.post(URL + add_book, json=location_map['book'])
    print(r.json())