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
    sort_movies(movies)
    user_input = input(f"{MENU}\n>>> ").upper()
    while user_input != 'Q':
        if user_input == 'L':
            show_movie(movies)
            user_input = input(f"{MENU}\n>>> ").upper()
        elif user_input == 'A':
            add_movie()
            user_input = input(f"{MENU}\n>>> ").upper()
        elif user_input == 'W':
            watch_movie(movies)
            user_input = input(f"{MENU}\n>>> ").upper()
        else:
            print("Invalid menu choice")
            user_input = input(f"{MENU}\n>>> ").upper()
    print("{} movies saved to movies.csv\nHave a nice day :)")


def show_movie(movies):
    watched_movie = 0
    unwatch_movie = 0
    for num, movie in enumerate(movies):
        if movie[3] == 'u':
            unwatch_movie = unwatch_movie + 1
            print(f"{num}. *  {movie[0]:<35} - {movie[1]:>4} ({movie[2]})")
        else:
            watched_movie = watched_movie + 1
            print(f"{num}.    {movie[0]:<35} - {movie[1]:>4} ({movie[2]})")
    print("{} movies watched, {} movies still to watch.".format(watched_movie, unwatch_movie))


def add_movie():
    pass


def watch_movie(movies):
    movie_choice = input("Enter the number of a movie to mark as watched\n>>> ")
    is_valid = False
    while not is_valid:
        try:
            movie_choice = int(movie_choice)
            if movie_choice > len(movies) - 1:
                print("Invalid movie number")
                movie_choice = input(">>> ")
            elif movie_choice < 0:
                print("Number must >= 0")
                movie_choice = input(">>> ")
            else:
                is_valid = True
        except ValueError:
            print("Invalid input; enter a valid number")
            movie_choice = input(">>>")

    movie = movies[movie_choice]
    if movie[3] == 'u':
        print(f"{movie[0]} form {movie[1]} watched")
        movie[3] = 'w'
    else:
        print(f"You have already watched {movie[0]}")


def sort_movies(movies):
    for movie in movies:
        movie[1] = int(movie[1])
    movies.sort(key=lambda x: (x[1], x[2]))


def load_movies():
    movies = open("movies.csv", 'r')
    movie_list = []
    for line in movies:
        movie = line.strip().split(',')
        movie_list.append(movie)
    return movie_list


main()
