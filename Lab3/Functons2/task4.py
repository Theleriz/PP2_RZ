def average_imdb(moviess):
    if not moviess:
        return 0; 
    total_s = sum(movie["imdb"] for movie in moviess)
    return total_s / len(moviess)