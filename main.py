import sys
import ner_service
import text_processor

def main():
	# input = sys.argv[1]
	# text = file(input, 'r').read()
	'''To be added later '''
	text = open('sample_text.txt', 'r', encoding = 'utf-8').read()
	text_to_process = ner_service.get_ner_response(text)
	print(text_processor.get_locations(text_to_process))


if __name__ == '__main__':
	main()