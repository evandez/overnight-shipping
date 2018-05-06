import csv
import googlemaps

GOOGLE_MAPS_API_KEY = ''

road_map = {
    'Seattle': ['Chicago', 'Portland', 'Denver'],
    'Portland': ['San Francisco', 'Seattle', 'Denver'],
    'San Francisco': ['Portland', 'San Jose', 'Denver', 'Los Angeles'],
    'San Jose': ['San Francisco', 'Denver', 'Las Vegas', 'Los Angeles'],
    'Los Angeles': ['San Francisco', 'San Jose', 'Las Vegas', 'San Diego'],
    'San Diego': ['Los Angeles', 'Tucson'],
    'Las Vegas': ['San Jose', 'Los Angeles', 'Phoenix AZ', 'Dallas'],
    'Phoenix AZ': ['Las Vegas', 'Tucson'],
    'Tucson': ['Phoenix AZ', 'San Diego', 'San Antonio', 'Dallas'],
    'Denver': ['Seattle', 'Chicago', 'Dallas', 'Las Vegas', 'San Francisco', 'San Jose', 'Portland'],
    'Dallas': ['Denver', 'Austin', 'Chicago', 'New Orleans', 'Las Vegas', 'Tucson', 'Houston'],
    'Austin': ['Dallas', 'San Antonio', 'Houston'],
    'San Antonio': ['Tucson', 'Houston', 'Austin'],
    'Houston': ['Dallas', 'Austin', 'San Antonio', 'New Orleans'],
    'Chicago': ['Denver', 'Seattle', 'Dallas', 'Memphis', 'Indianapolis', 'Washington DC', 'Philadelphia', 'Baltimore', 'Newark'],
    'Indianapolis': ['Chicago', 'Washington DC', 'Atlanta GA', 'Memphis'],
    'Memphis': ['Chicago', 'Indianapolis', 'Atlanta GA', 'New Orleans'],
    'New Orleans': ['Dallas', 'Houston', 'Jacksonville FL', 'Atlanta GA', 'Memphis'],
    'Atlanta GA': ['Memphis', 'New Orleans', 'Indianapolis', 'Jacksonville FL'],
    'Jacksonville FL': ['Washington DC', 'Tampa', 'Miami'],
    'Tampa': ['Jacksonville FL', 'Miami'],
    'Miami': ['Tampa', 'Jacksonville FL'],
    'Washington DC': ['Chicago', 'Indianapolis', 'Jacksonville FL', 'Baltimore'],
    'Baltimore': ['Washington DC', 'Philadelphia'],
    'Philadelphia': ['Newark', 'Baltimore'],
    'Newark': ['New York City', 'Philadelphia'],
    'New York City': ['Boston', 'Newark'],
    'Boston': ['New York City', 'Chicago'],
    'Honolulu': [],
    'Anchorage': []
}
fixed = {
    'Phoenix AZ': 'Phoenix',
    'Atlanta GA': 'Atlanta',
    'Jacksonville FL':'Jacksonville'
}

dist_matrix = {}
gmaps = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)
for i in road_map.keys():
    matrix = ''
    try:
        print('Processing: ', i)
        if not road_map[i]:
            continue
        matrix = gmaps.distance_matrix(origins=i, destinations=road_map[i], mode='driving', language='en-US', units='imperial')
        distances = [float(i['distance']['text'].replace(',', '').replace('mi', '').strip()) for i in matrix['rows'][0]['elements']]
        if i not in dist_matrix:
            dist_matrix[i] = {}

        for j, k in enumerate(road_map[i]):
            dist_matrix[i][k] = distances[j]
    except Exception as e:
        print('Failed on: ', i, 'Data: ', str(matrix))
        continue

city_list = list(road_map.keys())
city_list.sort()
csv_text = ',' + ','.join([(fixed[city] if city in fixed else city) for city in city_list]) + '\n'
for i in city_list:
    csv_text += (fixed[i] if i in fixed else i) + ','
    for j in city_list:
        dist = 1e12
        if i in dist_matrix and j in dist_matrix[i]:
            dist =  dist_matrix[i][j]
        elif j in dist_matrix and i in dist_matrix[j]:
            dist = dist_matrix[j][i]
        elif i == j:
            dist = 0
        csv_text += str(dist) + ','
    csv_text += '\n'

with open('road_distances.csv', 'w+') as f:
    f.write(csv_text)
