""" Oefening 5 (  / 6 )
Maak onderstaande boekenwinkel-app verder af.
Het menu is reeds gemaakt. Jij zal de opties in dit menu verder uitwerken.

Er zijn 3 opties waaruit de bediende kan kiezen.
Alle opties maken gebruik van de dictionary catalogus.
    1) Toon details van boek.
    2) Voeg boek toe (aan dictionary catalogus).
    3) Geef overzicht van catalogus.

"""

catalogus = { # De start-catalogus van de boekenwinkel.
    'The Foundation': {'auteur': 'Asimov', 'datum': '1951'},
    '2001: A Space Odyssey': {'auteur': 'Clarke', 'datum': '1968'},
    'Rocketship Galileo': {'auteur': 'Heinlein', 'datum': '1947'},
}

while True: # Start de app.
    # Overzicht keuzemenu
    print("Menu: ")
    print("  1) Toon details van boek.")
    print("  2) Voeg boek toe.")
    print("  3) Toon catalogus.")
    print("  4) Stop de app.")

    # Kies een van de 4 opties.
    optie = input("Selecteer wat je wilt doen: ")

    if optie == "1":   # Toon details van opgevraagd boek.
        """ 1) Toon details van boek.
        Vraag de gebruiker naar de titel van een boek.

        Komt het boek voor in de dictionary catalogus, print dan alle informatie als volgt.
            >>> Het boek *titel* is geschreven door *auteur* en gepubliceerd in *datum*.

        Als het boek niet voorkomt in de dictionary catalogus, print dan het volgende.
            >>> Kan boek *titel* niet vinden.
        """
        titel = input("Geef de titel van het boek: ")
        if titel in catalogus:
            boek_info = catalogus[titel]
            auteur = boek_info['auteur']
            datum = boek_info['datum']
            print(f"Het boek {titel} is geschreven door {auteur} en gepubliceerd in {datum}.")
        else:
            print(f"Kan boek {titel} niet vinden")

    elif optie == "2": # Voeg boek toe aan de dictionary catalogus.
        """ 2) Voeg boek toe.
        Vraag de gebruiker om een *titel*, *auteur* & *publicatiedatum*.
        Voeg vervolgens een nieuw element toe aan de dictionary catalogus. Dit element 
        heeft als sleutel de *titel*, de waarde is een sub-dict met de overige info.

        Het element ziet er dus in het algemeen als volgt uit.
            *titel*: {'auteur': *auteur*, 'datum': *publicatiedatum*}
        Een specifiek voorbeeld is.
            'The Foundation': {'auteur': 'Asimov', 'datum': '1951'}

        Het is toegelaten om een titel die reeds bestaat in de catalogus te overschrijven.
        """
        titel = input("Voer de titel van het boek in: ")
        auteur = input("Voer de auteur van het boek in: ")
        datum = input("Voer de publicatiedatum van het boek in: ")
        catalogus[titel] = {'auteur': auteur, 'datum': datum}
        print(f"Het boek {titel} is toegevoegd aan de catalogus.")


    elif optie == "3":
        """ 3) Geef overzicht van catalogus.
        Print ieder boek (met auteur) dat zich in de dictionary catalogus bevindt.
        De print moet als volgt eruitzien.
            >>> Volgende boeken staan momenteel in de catalogus:
            >>>     - The Foundation (Asimov)
            >>>     - 2001: A Space Odyssey (Clarke)
            >>>     - Rocketship Galileo (Heinlein)
            >>>     - enzoverder voor ieder ander boek in de catalogus...
        """
        print("\nVolgende boeken staan momenteel in de catalogus:")
        for titel, boek in catalogus.items():
            auteur = boek['auteur']
            print(f"  - {titel} ({auteur})")

    elif optie == "4": # Stop de app.
        print(f"\nBedankt voor het gebruiken van deze app.")
        break

    else: # Verkeerde input gegeven.
        print(f"\nDit is geen optie. Gelieve opnieuw te proberen.")
        