import json
try:
    bestand_boodschappen = r"hfst_4/oefenmee/oefenmee_8.json"

    with open(bestand_boodschappen, 'r') as file:
        boodschappen = json.load(file)

    fruit = input("Van welk fruit wil je de hoeveelheid weten: ")
    aantal = int(boodschappen[fruit])
    print(f"Er staan {aantal} {fruit} op de lijst.")

except KeyError:
    print("De vrucht die u koos staat niet in de lijst.")

except FileNotFoundError:
    print("Het bestand wat u oproept kan niet gevonden worden.")
