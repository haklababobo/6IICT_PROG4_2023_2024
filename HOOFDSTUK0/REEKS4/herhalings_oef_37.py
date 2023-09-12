""" Maak het spel galgje na.

    Gebruik hiervoor een willekeurig woord uit 
    onderstaande lijst (uitbreiden mag).

    Vraag de gebruiker naar een letter of
    om het woord te raden. Het spel stopt
    als het woord correct is of na 7 vragen.

    Print in het eerste geval "gewonnen!".
    In het tweede geval "verloren!". 

        Tip! stel een lijst op met erin de
             gevonden letters. Vul deze eerst
             volledig met _ . Als de gebruiker een 
             letter geeft die in het woord zit, 
             vervang de overeenkomstige _ door deze 
             letter.

    >>> Gok letter / Raad woord (1/7): a
    Woord:  _  _  _  _
    >>> Gok letter / Raad woord (2/7): e
    Woord:  e  _  e  _
    >>> Gok letter / Raad woord (3/7): t
    Woord:  e  _  e  _
    >>> Gok letter / Raad woord (4/7): v
    Woord:  e  v  e  _
    >>> Gok letter / Raad woord (5/7): even
    gewonnen!
"""

import random

woorden = ["uier", "even", "stuk", "volk"]
woord = random.choice(woorden)
gevonden_letters = ["_"] * len(woord)
max_pogingen = 7
poging = 1

def toon_status():
    print(f"Woord: {' '.join(gevonden_letters)}")

while poging <= max_pogingen:
    print(f">>> Gok letter / Raad woord ({poging}/{max_pogingen}):")
    gok = input().lower()

    if len(gok) == 1 and gok.isalpha():
        if gok in woord:
            for i in range(len(woord)):
                if woord[i] == gok:
                    gevonden_letters[i] = gok
            toon_status()
        else:
            toon_status()
    elif len(gok) == len(woord) and gok.isalpha():
        if gok == woord:
            print("Gewonnen!")
            break
        else:
            toon_status()
    else:
        print("Ongeldige invoer. Voer een enkele letter in of probeer het hele woord.")

    poging += 1

if ''.join(gevonden_letters) == woord:
    print("Gewonnen!")
else:
    print("Verloren! Het juiste woord was:", woord)
