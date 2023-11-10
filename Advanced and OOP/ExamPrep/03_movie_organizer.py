def movie_organizer(*movies):
    genres_dict = {}
    for movie_name, genre in movies:
        if genre not in genres_dict:
            genres_dict[genre] = []
        genres_dict[genre].append(movie_name)
    sorted_film_genres = sorted(genres_dict.items(), key=lambda x: (-len(x[1]), x[0]))
    result = ""

    for genre, movie_name in sorted_film_genres:
        sorted_movies = sorted(movie_name)
        result += f"{genre} - {len(sorted_movies)}\n"
        for name in sorted_movies:
            result += f"* {name}\n"
    return result.strip()


print(movie_organizer(
    ("The Matrix", "Sci-fi")))
