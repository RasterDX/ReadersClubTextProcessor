import requests
from clustering_service import cluster

URL = "https://readers-club-api.herokuapp.com/"

add_book = "books/add"
add_loc = ""

def persist_locations(location_map):
    location_map['book']['locations'] =  cluster(location_map['book']['locations'])
    r = requests.post(URL + add_book, json=location_map['book'])
