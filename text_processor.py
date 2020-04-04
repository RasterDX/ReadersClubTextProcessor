def unique_list(list):
    unique_list = []   
    for x in list:
        if x not in unique_list: 
            unique_list.append(x) 
    return unique_list

def get_locations(text):
	encoded = text
	lines = encoded.splitlines()
	locuri = ['Cabana', 'Manastirea', 'Poiana', 'dealul', 'varful', 'gara', 'Rezervatia']
	places = []


	# for i in range(1, len(lines)):
	# 	if ('LOC' in lines[i] and 'LOC' in lines[i-1]) or ('ORG' in lines[i] and 'ORG' in lines[i-1]):
	# 		result = lines[i-1].split('\t',1)[0] + ' ' + lines[i].split('\t',1)[0]
	# 		places.append(result)
	# 		result = ''
	# 	elif 'LOC' in lines[i] and 'Spsa' in lines[i-1] and 'LOC' in lines[i-2]:
	# 		result = lines[i-2].split('\t',1)[0] + ' ' + lines[i-1].split('\t',1)[0] + ' ' + lines[i].split('\t',1)[0]
	# 		places.append(result)
	# 		result = ''
	# 	elif 'LOC' in lines[i] and 'LOC' not in lines[i+1] and 'LOC' not in lines[i-1] and 'Spsa' not in lines[i+1]:
	# 		result = lines[i].split('\t',1)[0]
	# 		if(result[0].isupper()):
	# 			places.append(result)


	for i in range (1, len(lines)-2):
		if ('ORG' in lines[i] and 'ORG' in lines[i+1] and 'Ds' in lines[i+2] and 'ORG' in lines[i+3] and 'ORG' in lines[i+4]):
			result = lines[i].split('\t',1)[0] + ' ' + lines[i+1].split('\t',1)[0] + ' ' + lines[i+2].split('\t',1)[0] + ' ' + lines[i+3].split('\t',1)[0] + ' ' + lines[i+4].split('\t',1)[0]
			places.append(result)
			result = ''
		if ('PER' in lines[i] and 'PER' in lines[i+1] and 'Ds' in lines[i+2] and 'LOC' in lines[i+3] and 'PER' in lines[i+4]):
			result = lines[i].split('\t',1)[0] + ' ' + lines[i+1].split('\t',1)[0] + ' ' + lines[i+2].split('\t',1)[0] + ' ' + lines[i+3].split('\t',1)[0] + ' ' + lines[i+4].split('\t',1)[0]
			places.append(result)
			result = ''
		if ('ORG' in lines[i] and 'Sp' in lines[i+1] and 'ORG' in lines[i+2] and 'ORG' in lines[i+3]):
			result = lines[i].split('\t',1)[0] + ' ' + lines[i+1].split('\t',1)[0] + ' ' + lines[i+2].split('\t',1)[0] + ' ' + lines[i+3].split('\t',1)[0]
			places.append(result)
			result = ''
		if ('PER' in lines[i] and 'PER' in lines[i+1] and lines[i].split('\t',1)[0] in locuri) or ('LOC' in lines[i] and 'LOC' in lines[i+1] and lines[i].split('\t',1)[0] in locuri) or ('ORG' in lines[i] and 'ORG' in lines[i+1] and lines[i].split('\t',1)[0] in locuri):
			result = lines[i].split('\t',1)[0] + ' ' + lines[i+1].split('\t',1)[0]
			places.append(result)
			result = ''
		if('O' in lines[i] and 'PER' in lines[i+1] and lines[i].split('\t',1)[0] in locuri and '.' not in lines[i+1].split('\t',1)[0]):
			result = lines[i].split('\t',1)[0] + ' ' + lines[i+1].split('\t',1)[0]
			if ('.' in result):
				places.append(result.replace('.', '').strip())
			else:
				places.append(result)
				result = ''
		if ('O' in lines[i] and 'PER' in lines[i+1] and 'PER' in lines[i+2] and lines[i].split('\t',1)[0] in locuri and lines[i].split('\t',1)[0] != 'varful' and '.' not in lines[i+1].split('\t',1)[0]):
			result = lines[i].split('\t',1)[0] + ' ' + lines[i+1].split('\t',1)[0] + ' ' + lines[i+2].split('\t',1)[0]
			if ('.' in result):
				places.append(result.replace('.', '').strip())
			else:
				places.append(result)
				result = ''
	# return places
	return unique_list(places)

