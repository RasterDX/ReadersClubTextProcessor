import sys
import ner_service
import text_processor
import requests

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
	# input = sys.argv[1]
	# text = file(input, 'r').read()
	'''To be added later '''
	# text = open('sample_text.txt', 'r', encoding = 'utf-8').read()
	# text_to_process = ner_service.get_ner_response(text)
	
	# locations = text_processor.get_locations(text_to_process)
	# print(locations)

	locations = ['Rezervatia Geologica si Paleontologica Repedea', 'Rezervatia Geologica',
	 	'Parcul de aventura Hamak', 'Manastirea Cetatuia', 'Manastirea Hadambu', 'Rezervatia Repedea', 'Poiana Rotunda',
		'Cabana Barnova', 'dealul Repedea', 'varful Movila', 'varful Slobozia-Cantemir', 'gara Barnova']

	print('starting google places api requests')


	for location in locations:
		params_get['input'] = location
		resp = requests.get(url = PLACES_API_URL, params = params_get) 
		# the api returns a list of candidates
		data = resp.json()['candidates']
		#the best candidates beings the first one (we can explore others)
		best_cand = data[0]
		print('input: ', location.encode('utf-8'), ' best_find: ', best_cand['name'].encode('utf-8'), best_cand['geometry']['location'])

		


if __name__ == '__main__':
	main()