import csv

air_routes = {
    'Anchorage': ['Seattle', 'Portland'],
    'Honolulu': ['Los Angeles', 'San Francisco'],
    'Seattle': ['Chicago', 'Portland', 'Los Angeles'],
    'Portland': ['Seattle', 'Chicago', 'San Francisco'],
    'San Francisco': ['Portland', 'Honolulu', 'Denver', 'Los Angeles'],
    'Los Angeles': ['Honolulu', 'Denver', 'Atlanta', 'Chicago'],
    'San Diego': ['Dallas'],
    'Atlanta': ['Los Angeles', 'Dallas', 'Washington DC', 'Miami'],
    'Chicago': ['New York City', 'Washington DC', 'Seattle', 'Portland', 'Denver', 'Los Angeles', 'Atlanta', 'Memphis'],
    'Dallas': ['Chicago', 'Memphis'],
    'Memphis': ['Chicago', 'Dallas'],
    'Miami': ['Atlanta', 'Washington DC'],
    'Washington DC': ['Chicago', 'New York City', 'Atlanta', 'Miami'],
    'New York City': ['Washington DC', 'Chicago']
}

with open('raw_air_distances.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    raw_matrix = [row for row in reader]
    cities = raw_matrix[0][1:]
    distances = [[float(item) for item in row[1:]] for row in raw_matrix[1:]]

    with open('air_distances.csv', 'w+') as outf:
        outf.write(',' + ','.join(cities) + '\n')
        for i in cities:
            outf.write(i + ',')
            for j in cities:
                i_index = cities.index(i)
                j_index = cities.index(j)
                d = 1e12
                if i in air_routes and j in air_routes[i]:
                    d = distances[i_index][j_index]
                elif j in air_routes and i in air_routes[j]:
                    d = distances[j_index][i_index]
                elif i == j:
                    d = 0
                outf.write(str(d) + ',')
            outf.write('\n')
