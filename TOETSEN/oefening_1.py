""" OEFENING 1 (   / 1.5)
Onderstaande code implementeert het spel hoger-lager.
Momenteel crasht dit spel alleen als de input van de gebruiker geen geheel getal is.

Het is aan jullie om ook exceptions te laten optreden (raisen) in andere gevallen.
    - Getal is kleiner dan 0 of hoger dan 100. 
    - Gebruiker geeft een getal op dat deze al heeft opgegeven (zie variabele gegokte_getallen)
    - Na 8 pogingen (v).
Gebruik hiervoor Custom Exceptions (je mag naam & uitleg zelf kiezen).

"""

import random

class InvalidGuessError(Exception):
    pass

class OutOfBoundsError(Exception):
    pass

class DuplicateGuessError(Exception):
    pass

class MaxAttemptsExceededError(Exception):
    pass

def start_hogerlager():
    # Verwelkom speler & leg spel uit.
    print("Welkom bij het spel hoger-lager. Probeer zo snel mogelijk het geheime getal te raden.")
    print(f"Dit is een getal tussen 0 en 100. Veel success!\n")

    # Bepaal geheim getal & zet wat variabelen klaar.
    geheim_getal = random.randint(0, 100)
    pogingen, gegokte_getallen = 0, []
    max_pogingen = 8

    while True:
        try:
            # Vraag gebruiker om getal.
            gegokt_getal = int(input(f"Wat is het geheime getal (poging: {pogingen+1}): "))

            # Controleer of dit getal hoger/lager is dan geheim getal (en print dit).
            # Anders als het getal correct is, stop de while-loop.
            if gegokt_getal < 0 or gegokt_getal > 100:
                raise OutOfBoundsError("Het getal moet tussen 0 en 100 liggen.")
            elif gegokt_getal in gegokte_getallen:
                raise DuplicateGuessError("Je hebt dit getal al eerder geraden.")
            elif pogingen >= max_pogingen:
                raise MaxAttemptsExceededError("wie is er zo slecht in hoger-lager?.")
            elif gegokt_getal < geheim_getal:
                print("Je zult wat hoger moeten gokken!")
            elif gegokt_getal > geheim_getal:
                print("Fout, zoek het wat lager!")
            else:
                break

            # Verhoog het aantal pogingen met 1 & voeg het gegokte getal toe aan een lijst.
            pogingen += 1
            gegokte_getallen.append(gegokt_getal)

        except ValueError:
            print("Ongeldige invoer. Voer een geheel getal in.")
        except OutOfBoundsError as error:
            print(f"Fout: {error}")
        except DuplicateGuessError as error:
            print(f"Fout: {error}")
        except MaxAttemptsExceededError as error:
            print(f"Fout: {error}")
            break

    # Na getal te raden. Print wat regels...
    if gegokt_getal == geheim_getal:
        print(f"Goed zo! Het getal was inderdaad {gegokt_getal}")
        print(f"Je had {pogingen} nodig om het getal te raden.")
    else:
        print(f"Helaas, je hebt het geheime getal niet kunnen raden. Het was {geheim_getal}.")

start_hogerlager()
