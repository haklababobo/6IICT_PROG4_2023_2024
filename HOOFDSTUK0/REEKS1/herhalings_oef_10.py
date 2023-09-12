def favoriete_taal(antwoord):
    "PRINT 'goeie keuze' als 'Python' IN antwoord zit"
    if 'Python' in antwoord:
        print("goeie keuze")

favoriete_taal("Dat is C++")          # (niets wordt afgedrukt)
favoriete_taal("Ik vind Python leuk") # goeie keuze
favoriete_taal("Zeker weten Java")    # (niets wordt afgedrukt)
