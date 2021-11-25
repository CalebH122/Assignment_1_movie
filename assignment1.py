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
    original_movies = load_movies()
    user_input = input(f"{MENU}\n>>> ").upper()
    while user_input != 'Q':
        if user_input == 'L':
            movie_list = show_movie()
        elif user_input == 'A':
            new_movie = add_movie()
        elif user_input == 'W':
            movie_watched = watch_movie()
        else:
            print("Invalid menu choice")
            user_input = input(f"{MENU}\n>>> ").upper()
    print("{} movies saved to movies.csv\nHave a nice day :)")


def load_movies():
    movies = open("movies.csv", 'r')
    movie_list = []
    for movie in movies:
        movie_list.append(movie)
    return movie_list


main()
