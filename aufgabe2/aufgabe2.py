import sys

filename = sys.argv[1]
if filename[-4:] != ".txt":
    filename += ".txt"

try:
    my_file = open(filename, 'r')

    movies = []
    title = str()

    for line in my_file:
        if line.startswith("#movielist"):
            line = next(my_file)
            tag, title = line.strip().split(': ', 1)
            line = next(my_file)

        if line.startswith("#movie"):
            movie = dict()
            movie['count'] = 0
            for i in range(0, 3):
                line = next(my_file, i)
                key, value = line.strip().split(':', 1)

                movie[key] = value.strip()
            movies.append(movie)

    movies.sort(key=lambda k: k['date'], reverse=True)
    # sorted from most recent access to least recent


    output = []
    for item in movies:
        if item['name'] not in output:
            output.append(item['name'])

    print(title + "\n===============\nNo. of Entries: %d\nNo. of Movies: %d\n" % (len(movies), len(output)))
    for item in output:
        print(item)


except IOError:
    print("file doesn't exist")
