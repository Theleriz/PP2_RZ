from task3 import in_category
from task4 import average_imdb

def average_imdb_score(movies, category):
    category_movies = in_category(movies, category)
    return average_imdb(category_movies)