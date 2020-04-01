import sys
import request
import text_processor

def main():
	# input = sys.argv[1]
	# text = file(input, 'r').read()
	'''To be added later '''
	text = 'Am mers cu Andreea la Palatul Culturii, apoi am urcat spre Piata Unirii. Dupa ce am plecat din piata am coborat spre Gara. In final ne-am pornit spre Muzeul de Arta.'
	text_to_process = request.get_ner_response(text)
	print(text_processor.get_locations(text_to_process))


if __name__ == '__main__':
	main()