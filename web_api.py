import requests
from clustering_service import cluster

URL = "http://localhost:8080/"
# URL = "https://readers-club-api.herokuapp.com/"

add_book = "books/add"
add_loc = ""

def persist_locations(location_map):
    clustered_locations = cluster(location_map['book']['locations'])
    r = requests.post(URL + add_book, json=location_map['book'])
    print(r.json())