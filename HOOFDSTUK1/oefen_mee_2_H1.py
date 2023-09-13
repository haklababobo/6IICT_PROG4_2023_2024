fruitmand = { # Sleutel is fruit, waarde is aantal
    "appel": 5,
    "banaan": 3,
    "kers": 50
}

fruitmand["mango"] = 1 # Nieuw element toegevoegd
fruitmand["banaan"] = 8
fruitmand.pop("kers") # element verwijderd

print( fruitmand )