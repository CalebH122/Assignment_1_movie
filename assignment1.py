"""
Replace the contents of this module docstring with your own details
Name:
Date started:
GitHub URL:
"""

print("Movies to watch 1.0 - by Jiale Hou")

MENU = """L - List movie
A - Add new movie
W - Watch a movie
Q - Quit"""


def main():
    movie_list = load_movies()
    print(movie_list)


def load_movies():
    movies = open("movies.csv", 'r')
    movie_list = []
    for movie in movies:
        movie_list.append(movie)
    return movie_list


main()
