import requests


def get_ner_response(text):
    url = "http://89.38.230.23/ner/ner.php"
    data = {
        'text': text
    }
    response = requests.post(url, data)
    return response.text