import ner_service
import text_processor
import web_api
import requests
from os import listdir
from os.path import isfile, join

API_KEY = 'AIzaSyAHqyMfdLhmN2t-MeVv6lggmQPoxfDvY9U'

params_get =  {
	'output' : 'json',
	'key' : API_KEY,
	'inputtype' : 'textquery',
	'language' : 'ro',
	'fields' : 'name,geometry'
}

PLACES_API_URL = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"

def main():
	onlyfiles = [f for f in listdir('./texts') if isfile(join('./texts', f))]
	print("Selectati un text pentru a extrate locatiile:")
	for i in range(0, len(onlyfiles)):
		print(f"{i}\t{onlyfiles[i]}")
	selection = int(input("Select: "))
	try:
		text = open('./texts/' + onlyfiles[selection], 'r', encoding = 'utf-8').read()
	except:
		text = open('./texts/' + onlyfiles[selection], 'r').read()
	text_to_process = ner_service.get_ner_response(text)
	print(text_to_process)
	
	locations = text_processor.get_locations(text_to_process)
	print(locations)

	print('starting google places api requests')

	location_map = {
		'book': {
			'locations': []
		}
	}

	location_map['book']['title'] = input("Enter book name: ")
	location_map['book']['author'] = input("Enter book author: ")
	location_map['book']['coverUrl'] = input("Enter book cover url: ")
	location_map['book']['textModel'] = text

	for location in locations:
		if len(location) > 0:
			params_get['input'] = location
			resp = requests.get(url = PLACES_API_URL, params = params_get)
			# the api returns a list of candidates
			data = resp.json()['candidates']
			#the best candidates beings the first one (we can explore others)
			print(data)
			if len(data) > 0:
				best_cand = data[0]
				location_map['book']['locations'].append({
					'name': best_cand['name'],
					# 'name': location,
					'latitude': best_cand['geometry']['location']['lat'],
					'longitude': best_cand['geometry']['location']['lng']
				})
				print('input: ', location.encode('utf-8'), ' best_find: ', best_cand['name'].encode('utf-8'), best_cand['geometry']['location'])

	web_api.persist_locations(location_map)


if __name__ == '__main__':
	main()