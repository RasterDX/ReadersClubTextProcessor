import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import normalize
from sklearn.decomposition import PCA
from math import sin, cos, sqrt, atan2, radians
import statistics
from scipy.spatial import distance


def get_distance(lat1, lon1, lat2, lon2):
    R = 6373.0

    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c


def cluster(locations):
    locations = [dict(t) for t in {tuple(d.items()) for d in locations}]
    print("\n\n\n\n\nPRINTING LOCATIONS")
    print(locations)
    eps = 200
    distances = []
    for loc1 in locations:
        for loc2 in locations:
            if loc1 != loc2:
                distances.append(distance.euclidean((loc1['latitude'], loc1['longitude']), (loc2['latitude'], loc2['longitude'])))
    median = statistics.median(distances)/3
    dataset = pd.DataFrame(locations)
    print(dataset)
    dataset_temp = dataset[["latitude", "longitude"]]
    dataset_temp = StandardScaler().fit_transform(dataset_temp)
    db = DBSCAN(eps=0.5, min_samples=2)
    db.fit(dataset_temp)
    labels = db.labels_
    dataset["Cluster"] = labels
    locs = []
    for index, rows in dataset.iterrows():
        my_list = [rows.name, rows.latitude, rows.longitude]
        if rows.Cluster != -1:
            locs.append(dict({
                'name': locations[index]['name'],
                'latitude': rows.latitude,
                'longitude': rows.longitude
            }))
    print(labels)
    print(dataset)
    print(median)
    print(locs)
    print(len(locs))

    return locs