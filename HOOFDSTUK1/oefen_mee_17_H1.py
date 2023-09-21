# Niveau 1
inception_film = {
    'jaar': 2010,
    'genre': ['Actie', 'Sciencefiction', 'Thriller'],
    'cast': [ 
        {'acteur': 'Leonardo DiCaprio', 'rol': 'Cobb'},
        {'acteur': 'Joseph Gordon-Levitt', 'rol': 'Arthur'},
        {'acteur': 'Ellen Page', 'rol': 'Ariadne'}
    ],
    'locaties': ['Parijs', 'Los Angeles', 'Tokio'],
    'box_office': {'budget': 160000000, 'opbrengst': 829895144},
    'awards': {'Oscars': 0, 'Golden Globes': 4}
}

# Niveau 2
jaar = inception_film['jaar']
tweede_genre = inception_film['genre'][1]
opbrengst = inception_film['box_office']['opbrengst']
rol_leonardo_dicaprio = inception_film['cast'][0]['rol']

print(f"Het jaar dat de film uitkwam: {jaar}")
print(f"Het tweede element in de lijst met genres: {tweede_genre}")
print(f"De opbrengst van de film: {opbrengst}")
print(f"De rol van acteur Leonardo DiCaprio: {rol_leonardo_dicaprio}")

# Niveau 3
inception_film['awards']['Oscars'] = 4

# Niveau 4
inception_film['regisseur'] = 'Christopher Nolan'
inception_film['cast'].append({'acteur': 'Tom Hardy', 'rol': 'Eames'})

# Controleer de bijgewerkte dictionary
print(inception_film)
# Niveau 1
inception_film = {
    'jaar': 2010,
    'genre': ['Actie', 'Sciencefiction', 'Thriller'],
    'cast': [ 
        {'acteur': 'Leonardo DiCaprio', 'rol': 'Cobb'},
        {'acteur': 'Joseph Gordon-Levitt', 'rol': 'Arthur'},
        {'acteur': 'Ellen Page', 'rol': 'Ariadne'}
    ],
    'locaties': ['Parijs', 'Los Angeles', 'Tokio'],
    'box_office': {'budget': 160000000, 'opbrengst': 829895144},
    'awards': {'Oscars': 0, 'Golden Globes': 4}
}

# Niveau 2
jaar = inception_film['jaar']
tweede_genre = inception_film['genre'][1]
opbrengst = inception_film['box_office']['opbrengst']
rol_leonardo_dicaprio = inception_film['cast'][0]['rol']

print(f"Het jaar dat de film uitkwam: {jaar}")
print(f"Het tweede element in de lijst met genres: {tweede_genre}")
print(f"De opbrengst van de film: {opbrengst}")
print(f"De rol van acteur Leonardo DiCaprio: {rol_leonardo_dicaprio}")

# Niveau 3
inception_film['awards']['Oscars'] = 4

# Niveau 4
inception_film['regisseur'] = 'Christopher Nolan'
inception_film['cast'].append({'acteur': 'Tom Hardy', 'rol': 'Eames'})

# Controleer de bijgewerkte dictionary
print(inception_film)
