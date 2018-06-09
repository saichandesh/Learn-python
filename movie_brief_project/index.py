"""
Movie structure
"""

movie = {
    'name': 'The Matrix',
    'director': 'Wachowskis',
    'year': '1994',
    'location': '3F-14',
    'shelf': '3F'
}

movies = [movie]


def add_movie():
    name = input("Enter the movie name: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")
    location = input("Enter the movie release location: ")
    shelf = input("Enter the movie release shelf: ")

    movies.append({
        'name': 'titanic',
        'director': 'James Cameron',
        'year': 1997,
        'location': 'usa',
        'shelf': '3F'
    })


def view_all_movies():
    for m in movies:
        name, director, year, location, shelf = m.values()
        print(f'movie name: {name}')
        print(f'movie director: {director}')
        print(f'movie year: {year}')
        print(f'movie location: {location}')
        print(f'movie shelf: {shelf}')


def find_movie(key, value):
    found = []
    for m in movies:
        if m[key] == value:
            found.append(m)
    return found


def menu():
    user_input = input("Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit: ")
    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            view_all_movies()
        elif user_input == 'f':
            find_by = input("What property of the movie is that? ")
            looking_for = input("What are you looking for? ")
            movies_found = find_movie(find_by, looking_for)
            print(movies_found or 'No movies found.')
        else:
            print('Unknown command-please try again.')
            continue
        user_input = input("\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit: ")


menu()
