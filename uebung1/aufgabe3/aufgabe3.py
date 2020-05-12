import sys

filename = sys.argv[1]
if filename[-4:] != ".txt":
    filename += ".txt"

html = False
if len(sys.argv) > 2:
    html = True
    html_filename = sys.argv[2]

try:
    my_file = open(filename, 'r')
    movies = dict()
    title = str()

    for i, line in enumerate(my_file):
        if line.startswith("#movielist"):
            i += 1
            line = next(my_file)
            title = line.split(':')[1].strip()
        elif "file:" in line:
            movie_file = line.split(':')[1].strip()
        elif "name:" in line:  # and title not in line?
            movie_name = line.split(':')[1].strip()
            if movie_name in movies:
                movies[movie_name] = (movies[movie_name][0] + 1, movies[movie_name][1])
            else:
                movies[movie_name] = (1, movie_file)
            movie_file = str()

    if html:
        html_string = "<html>\n<head></head>\n<body>\n"
        html_string += "<h2>" + title + "</h2>\n"
        for movie in movies:
            html_string += movie + " (Angesehen: " + str(movies[movie][0]) + ", Datei: " + movies[movie][1] + ")<br>\n"
        html_string += "</body>\n</html>"

        new_file = open(html_filename, 'w')
        new_file.write(html_string)
        new_file.close()

except IOError:
    print("error, file doesn't exist")
