""" OEFENING 2 (   / 3.5)
In onderstaande code wordt gevraagd om een kluis te kiezen (zie JSON).
De code print de inhoud van deze kluis, en vraagt vervolgens om een voorwerp
toe te voegen aan de kluis & een voorwerp uit de kluis te verwijderen.
Tenslotte schrijft het de wijzigingen terug weg naar het JSON-bestand.

Via de while True blijft bovenstaande herhalen.
Dit tot de gebruiker "STOP" ingeeft, in plaats van een kluis te kiezen.


NIVEAU 1:

De code kan op verschillende wijzen fout gaan. Hiervoor is reeds een try-except
aangebracht. Deze simpele except geeft echter niet aan wat het exacte probleem is.
Pas de try-except aan door specifieke exceptions toe te voegen. 

Er moeten specifieke exceptions zijn voor volgende situaties:
    - JSON-bestand niet gevonden: print uitleg over probleem + stop programma (via exit).
    - Opgegeven kluis bestaat niet: print uitleg over probleem.
    - Te verwijderen voorwerp bestaat niet: print uitleg over probleem.

Enkel indien het JSON-bestand niet gevonden is, moet het programma stoppen.
In alle andere gevallen, gaat de while-loop dus gewoon verder.


NIVEAU 2:

Lukt het om de code ZONDER fouten te doorlopen. Print dan:
"De kluis is met succes gewijzigd!"


NIVEAU 3:

De nieuwe inhoud van de kluizen moet ALTIJD weggeschreven worden.
Dus ook als er midden in het programma een fout ontstaat, of de gebruiker
via CTRL+C expres het programma stopt.

Je kan dit testen door een voorwerp toe te voegen & vervolgens CTRL+C in te drukken.
Ondanks het crashen moet het toegevoegde voorwerp nog steeds in de JSON staan.

"""

import json

# Pad naar JSON-bestand & lege dict klaarzetten voor inhoud van kluisjes.
pad = "oef2_kluizen.json"
kluizen = {}

while True:
    try:
        # Haal inhoud van kluizen op uit JSON-bestand.
        try:
            with open(pad, "r") as fp:
                kluizen = json.load(fp)
        except FileNotFoundError:
            print(f"Het opgegeven JSON-bestand ({pad}) kon niet gevonden worden. Programma wordt afgesloten.")
            break

        # Vraag gebruiker om een kluis te kiezen
        # Het programma stopt wanneer de gebruiker STOP ingeeft, in plaats van een kluis.
        nummer_kluis = input("Welke kluis openen: ")
        if nummer_kluis.upper() == "STOP":
            break

        # Controleer of de opgegeven kluis bestaat
        if nummer_kluis not in kluizen:
            print(f"De opgegeven kluis ({nummer_kluis}) bestaat niet.")
            continue

        # Print inhoud van de gekozen kluis.
        print(f"In deze kluis zitten volgende zaken...")
        for voorwerp in kluizen[nummer_kluis]:
            print(f"    - {voorwerp}")

        # Vraag gebruiker om voorwerp toe te voegen aan kluis.
        voorwerp_toevoegen = input("Voorwerp toevoegen aan kluis: ")
        if voorwerp_toevoegen.strip() != "":
            kluizen[nummer_kluis].append(voorwerp_toevoegen)

        # Vraag gebruiker om voorwerp uit kluis te halen.
        voorwerp_verwijderen = input("Voorwerp verwijderen uit kluis: ")
        if voorwerp_verwijderen.strip() != "":
            if voorwerp_verwijderen not in kluizen[nummer_kluis]:
                print(f"Het opgegeven voorwerp ({voorwerp_verwijderen}) bestaat niet in de kluis.")
                continue
            kluizen[nummer_kluis].remove(voorwerp_verwijderen)

    except Exception as e:
        print(f"Er ging iets mis: {e}")
    finally:
        # Schrijf nieuwe inhoud van kluizen weg naar JSON-bestand, zelfs als er een fout optreedt.
        with open(pad, "w") as fp:
            json.dump(kluizen, fp)
