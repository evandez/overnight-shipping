import csv

# route loosely based on Class 1 Railroads in the US
# http://archive.freightrailworks.org/network/class-i/

train_routes = {
    'Seattle': ['Chicago', 'Portland', 'Denver'],
    'Portland': ['Seattle', 'San Francisco'],
    'San Francisco': ['Portland', 'San Jose'],
    'San Jose': ['San Francisco'],
    'Los Angeles': ['Denver', 'San Diego', 'San Jose'],
    'San Diego': ['Tucson', 'Los Angeles'],
    'Houston': ['New Orleans', 'Tucson'],
    'Tucson': ['San Diego', 'Houston'],
    'Denver': ['Chicago', 'Seattle', 'Dallas', 'Los Angeles'],
    'Dallas': ['Denver', 'Houston'],
    'New Orleans': ['Memphis', 'Houston', 'Jacksonville'],
    'Memphis': ['Chicago', 'New Orleans'],
    'Chicago': ['Denver', 'Seattle', 'Indianapolis', 'Memphis'],
    'Indianapolis': ['Chicago', 'Washington DC', 'Atlanta'],
    'Atlanta': ['Indianapolis', 'Jacksonville'],
    'Jacksonville': ['Tampa', 'Atlanta', 'Washington DC', 'New Orleans'],
    'Tampa': ['Jacksonville'],
    'Washington DC': ['Indianapolis', 'Washington DC', 'Philadelphia'],
    'Philadelphia': ['Newark', 'Washington DC'],
    'Newark': ['Philadelphia', 'New York City'],
    'New York City': ['Newark']
}

with open('raw_air_distances.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    raw_matrix = [row for row in reader]
    cities = raw_matrix[0][1:]
    distances = [[float(item) * 1.3 for item in row[1:]] for row in raw_matrix[1:]]

    with open('train_distances.csv', 'w+') as outf:
        outf.write(',' + ','.join(cities) + '\n')
        for i in cities:
            outf.write(i + ',')
            for j in cities:
                i_index = cities.index(i)
                j_index = cities.index(j)
                d = 1e12
                if i in train_routes and j in train_routes[i]:
                    d = distances[i_index][j_index]
                elif j in train_routes and i in train_routes[j]:
                    d = distances[j_index][i_index]
                elif i == j:
                    d = 0

                if d > 1e9:
                    d = '1E+12'

                outf.write(str(d) + ',')
            outf.write('\n')
