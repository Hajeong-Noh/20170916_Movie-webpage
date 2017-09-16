import media
import fresh_tomatoes

""" This file makes a list of movies and open a movie webpage """
im3 = media.Movie("Iron Man 3", "A story of a superhero in iron suit", "https://upload.wikimedia.org/wikipedia/en/d/d5/Iron_Man_3_theatrical_poster.jpg", "https://www.youtube.com/watch?v=f_h95mEd4TI")
tdk = media.Movie("Thor: The Dark World", "A story of a superhero with a hammer", "https://upload.wikimedia.org/wikipedia/en/7/7e/Thor_-_The_Dark_World_poster.jpg", "https://www.youtube.com/watch?v=npvJ9FTgZbM")
caws = media.Movie("Captain America: The Winter Soldier", "A story of a superhero with a shield", "https://upload.wikimedia.org/wikipedia/en/e/e8/Captain_America_The_Winter_Soldier.jpg", "https://www.youtube.com/watch?v=tbayiPxkUMM")
gg = media.Movie("Guardians of the Galaxy", "A story of superheros with in the universe", "https://upload.wikimedia.org/wikipedia/en/thumb/8/8f/GOTG-poster.jpg/220px-GOTG-poster.jpg", "https://www.youtube.com/watch?v=d96cjJhvlMA")
aau = media.Movie("Avengers: Age of Ultron", "A story of superheros against an evil creature", "https://upload.wikimedia.org/wikipedia/en/1/1b/Avengers_Age_of_Ultron.jpg", "https://www.youtube.com/watch?v=tmeOjFno6Do")
am = media.Movie("Ant-Man", "A story of a superhero who can make himself as small as ants", "https://upload.wikimedia.org/wikipedia/en/7/75/Ant-Man_poster.jpg", "https://www.youtube.com/watch?v=pWdKf3MneyI")

movies = (im3, tdk, caws, gg, aau, am)
fresh_tomatoes.open_movies_page(movies)
