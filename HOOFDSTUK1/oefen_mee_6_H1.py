# Dictionary met filmscores
filmscores = {
    "godfather": 9,
    "avatar": 3,
    "oppenheimer": 7.5
}

# Doorloop de dictionary en druk de zinnen af
for film, score in filmscores.items():
    print(f"De film {film} kreeg een score van {score} op 10.")
