def unique_list(list):
    unique_list = []
    for x in list:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list


def get_locations(text):
    lines = text.splitlines()
    processed_lines = []

    places = []

    for item in lines:
        line = []
        words = item.split('\t')
        for x in words:
            line.append(x)
        processed_lines.append(line)
    # print(actual_lines)
    place = []
    for index in range(0, len(processed_lines)):
        if 'LOC' in processed_lines[index] or 'ORG' in processed_lines[index] or ('PER' in processed_lines[index] and len(place) > 0):
            place.append(processed_lines[index][0])
        else:
            if len(place) > 0:
                places.append(' '.join(place))
                place = []
    return unique_list(places)