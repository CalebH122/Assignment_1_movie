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
    movies = load_movies()
    user_input = input(f"{MENU}\n>>> ").upper()
    while user_input != 'Q':
        if user_input == 'L':
            movie_list = show_movie(movies)
            user_input = input(f"{MENU}\n>>> ").upper()
        elif user_input == 'A':
            new_movie = add_movie()
            user_input = input(f"{MENU}\n>>> ").upper()
        elif user_input == 'W':
            movie_watched = watch_movie()
            user_input = input(f"{MENU}\n>>> ").upper()
        else:
            print("Invalid menu choice")
            user_input = input(f"{MENU}\n>>> ").upper()
    print("{} movies saved to movies.csv\nHave a nice day :)")


def show_movie(movies):
    watched_movie = 0
    unwatch_movie = 0
    for num, line in enumerate(movies):
        movie = line.strip().split(',')
        if movie[3] == 'u':
            unwatch_movie = unwatch_movie + 1
            print(f"{num}. *  {movie[0]:<35} - {movie[1]:>4} ({movie[2]})")
        else:
            watched_movie = watched_movie + 1
            print(f"{num}.    {movie[0]:<35} - {movie[1]:>4} ({movie[2]})")
    print("{} movies watched, {} movies still to watch.".format(watched_movie, unwatch_movie))


def add_movie():
    pass


def watch_movie():
    pass


def load_movies():
    movies = open("movies.csv", 'r')
    movie_list = []
    for movie in movies:
        movie_list.append(movie)
    return movie_list


main()
