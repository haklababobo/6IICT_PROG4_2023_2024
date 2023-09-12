""" Vraag een gebruiker naar wat deze wilt doen.
    Voeg het antwoord toe aan een lijst.

    Blijf de vraag stellen (en antwoord opslaan),
    tot de gebruiker "STOP" ingeeft.

    Print hierna een opsomming met de lijst.

    >>> Wat wil je doen: Bowlen
    >>> Wat wil je doen: Zwemmen
    >>> Wat wil je doen: Fietsen
    >>> Wat wil je doen: STOP

    Je hebt volgende zaken gepland:
        - Bowlen
        - Zwemmen
        - Fietsen
"""
# Maak een lege lijst om de activiteiten op te slaan
activiteiten = []

# Blijf vragen om input tot de gebruiker "STOP" invoert
while True:
    activiteit = input("Wat wil je doen: ")
    if activiteit.upper() == "STOP":
        break  # Stop de lus als "STOP" wordt ingevoerd
    activiteiten.append(activiteit)

# Print de lijst met geplande activiteiten
print("\nJe hebt volgende zaken gepland:")
for activiteit in activiteiten:
    print(f"- {activiteit}")
