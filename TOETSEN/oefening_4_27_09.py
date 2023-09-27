""" Oefening 4: (   / 3 )
Onderstaande dictionary toont een weervoorspelling voor Brussel. 
Onder de dictionary zijn de opgaves van deze oefening te vinden.
"""

weer_data = {
    "locatie": "Brussel",
    "huidig_weer": {
        "temp": 220, "vochtigheid": 65, "omstandigheden": "Deels bewolkt",
    },
    "voorspelling": {
        "vandaag": {
            "hoge_temp": 24, "lage_temp": 16, "overig": ["10% kans op regen", "Wind: 5 km/u"],
        },
        "morgen": {
            "hoge_temp": 25, "lage_temp": 17, "overig": ["Geen neerslag verwacht", "Wind: 7 km/u"],
        },
        "overmorgen": {
            "hoge_temp": 23, "lage_temp": 15, "overig": ["40% kans op regen", "Wind: 10 km/u"],
        },
    },
    "waarschreewingen": ["Hitteadvies", "Smog-gevaar", "tropische bui"],
}

""" 1)
Print de zin "40% kans op regen"" door deze op te halen uit de dictionary.
    Tip! Zoek de zin met behulp van CTRL + F.
"""
print(weer_data["voorspelling"]["overmorgen"]["overig"][0])

""" 2)
Het element "huidige_weer" bevat een fout. 
Ze geven hier een temp 220 graden celsius aan. Verander deze waarde naar 22.
"""
weer_data["huidig_weer"]["temp"] = 22

""" 3)
De sleutel "waarschreewingen" is verkeerd gespeld. Zorg ervoor dat dit
de sleutel "waarschuwingen" wordt. De waarde verbonden aan deze sleutel
moeten hetzelfde blijven.
"""
weer_data["waarschuwingen"] = weer_data.pop("waarschreewingen")

""" 4)
Print voor iedere dag in "voorspellingen" de hoogste temp.
De print moet er als volgt uitzien.

    Warmste temp voor de komende dagen:
        - vandaag: 24°C
        - morgen: 25°C
        - overmorgen: 23°C

Tip! Maak eerst een nieuwe variabele met de waarde van sleutel "voorspellingen".
     Overloop deze met een for-loop.
"""
voorspellingen = weer_data["voorspelling"]
print("Warmste temp voor de komende dagen:")
for dag, weer_info in voorspellingen.items():
    hoogste_temp = weer_info["hoge_temp"]
    print(f"- {dag}: {hoogste_temp}°C")