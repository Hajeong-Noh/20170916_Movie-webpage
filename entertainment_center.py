import media
import fresh_tomatoes


""" Iron Man 3 information """
im3 = media.Movie(
    "Iron Man 3", "A story of a superhero in iron suit",
    "https://upload.wikimedia.org/wikipedia/en/d/d5/Iron_Man_3_theatrical_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=f_h95mEd4TI"
    )

""" Thor: The Dark World information """
tdk = media.Movie(
    "Thor: The Dark World", "A story of a superhero with a hammer",
    "https://upload.wikimedia.org/wikipedia/en/7/7e/Thor_-_The_Dark_World_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=npvJ9FTgZbM"
    )

""" Captain America: The Winter Soldier information """
caws = media.Movie(
    "Captain America: The Winter Soldier", "A story of a superhero with a shield",  # NOQA
    "https://upload.wikimedia.org/wikipedia/en/e/e8/Captain_America_The_Winter_Soldier.jpg",  # NOQA
    "https://www.youtube.com/watch?v=tbayiPxkUMM"
    )

""" Guardians of the Galaxy """
gg = media.Movie(
    "Guardians of the Galaxy", "A story of superheros with in the universe",
    "https://upload.wikimedia.org/wikipedia/en/thumb/8/8f/GOTG-poster.jpg/220px-GOTG-poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=d96cjJhvlMA"
    )

""" Avengers: Age of Ultron """
aau = media.Movie(
    "Avengers: Age of Ultron", "A story of superheros against an evil creature",  # NOQA
    "https://upload.wikimedia.org/wikipedia/en/1/1b/Avengers_Age_of_Ultron.jpg",  # NOQA
    "https://www.youtube.com/watch?v=tmeOjFno6Do"
    )

""" Ant-Man information """
am = media.Movie(
    "Ant-Man", "A story of a superhero who can make himself as small as ants",
    "https://upload.wikimedia.org/wikipedia/en/7/75/Ant-Man_poster.jpg",
    "https://www.youtube.com/watch?v=pWdKf3MneyI"
    )

""" Put movie instances in movies list and call the
    fresh_tomatoes.open_movies_page function """
movies = (im3, tdk, caws, gg, aau, am)
fresh_tomatoes.open_movies_page(movies)
