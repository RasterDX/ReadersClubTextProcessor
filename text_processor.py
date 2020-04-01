

def get_locations(text):
	encoded = text.encode('utf-8')
	lines = encoded.splitlines()
	places = []
	for i in range(1, len(lines)):
		if ('LOC' in lines[i] and 'LOC' in lines[i-1]) or ('ORG' in lines[i] and 'ORG' in lines[i-1]):
			result = lines[i-1].split('\t',1)[0] + ' ' + lines[i].split('\t',1)[0]
			places.append(result)
			result = ''
		elif 'LOC' in lines[i] and 'Spsa' in lines[i-1] and 'LOC' in lines[i-2]:
			result = lines[i-2].split('\t',1)[0] + ' ' + lines[i-1].split('\t',1)[0] + ' ' + lines[i].split('\t',1)[0]
			places.append(result)
			result = ''
		elif 'LOC' in lines[i] and 'LOC' not in lines[i+1] and 'LOC' not in lines[i-1] and 'Spsa' not in lines[i+1]:
			result = lines[i].split('\t',1)[0]
			if(result[0].isupper()):
				places.append(result)
	return places
