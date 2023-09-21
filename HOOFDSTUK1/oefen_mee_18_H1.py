film_reviews = [
    {'Matrix': 9.2, 'Avatar': 8.8, 'Fury': 9.0, 'Skyfall': 8.1},
    {'Matrix': 3.5, 'Avatar': 1, 'Fury': 8, 'Skyfall': 4},
    {'Matrix': 10, 'Avatar': 3, 'Fury': 7, 'Skyfall': 5}
]

for i, review in enumerate(film_reviews, start=1):
    print(f'Persoon {i} gaf:')
    for film, score in review.items():
        print(f'    - {film} een {score} op 10.')
    