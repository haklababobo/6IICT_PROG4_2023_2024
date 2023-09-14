recept = {
    "Aardappelen": 800,
    "Wortelen": 500,
    "erwten": 300,
    "Worsten": 400
}

# Vraag aan de gebruiker voor hoeveel personen hij wil koken
aantal_personen = int(input("Voor hoeveel man kook je: "))

# Pas de hoeveelheid ingrediënten aan op basis van het aantal personen
for ingrediënt, hoeveelheid in recept.items():
    aangepaste_hoeveelheid = (hoeveelheid / 4) * aantal_personen
    aangepaste_hoeveelheid = int(aangepaste_hoeveelheid)  # Rond naar beneden af
    recept[ingrediënt] = aangepaste_hoeveelheid

# Print de titel van het aangepaste recept
print(f"Recept voor gehakt met wortelen en erwten voor {aantal_personen} personen.")

# Loop door de aangepaste ingrediënten en hoeveelheden en druk ze af
for ingrediënt, hoeveelheid in recept.items():
    print(f" - {ingrediënt}: {hoeveelheid} gr.")
