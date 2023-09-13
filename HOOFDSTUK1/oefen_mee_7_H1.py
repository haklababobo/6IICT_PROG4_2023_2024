# Dictionary met gasten en hun beroepen
gasten = {
    "Jan": "reporter",
    "Piet": "acteur",
    "Joris": "regisseur",
    "Korneel": "scenarist"
}

# Initialisatie van de while-loop
while True:
    naam = input("Geef de naam van de gast in (of STOP om te stoppen): ")

    # Controleer of de gebruiker wil stoppen
    if naam.upper() == "STOP":
        break

    # Controleer of de naam in de gastenlijst staat
    if naam in gasten:
        job = gasten.pop(naam)
        print(f"Welkom {job} {naam}. Kom binnen.")
    else:
        print(f"De naam {naam} staat niet op de lijst.")

# Einde van het script
