from Lab6.builtIN.task1 import goodMovie


def sublist(moviess):
    return[movie for movie in moviess if goodMovie(movie)]