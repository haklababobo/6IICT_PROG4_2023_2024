films = ["godfather", "avatar", "oppenheimer"]

scores = [9, 3, 10]

filmscores = {}

for index, film in enumerate(films):

    sleutel = film  # De sleutel is de huidige film.

    waarde = scores[index]  # De waarde is de overeenkomstige score.

    filmscores[sleutel] = waarde# Gebruik sleutel/waarde om nieuw dict element te maken. 

print(filmscores)