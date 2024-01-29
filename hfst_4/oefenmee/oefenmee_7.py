fruit_lijst = ["Appel", "Banaan", "Kers"]
try:
    getal = input( "Geef een getal: " )
    if "." in getal:
        getal = float( getal )
    else:
        getal = int( getal )
    print( fruit_lijst[getal] )
except IndexError:
    print("te hoog getal voor de lijst")
except ValueError:
     print("Je kan enkel getallen ingeven")
except Exception:
    print("Er is een foutje")
print("Programma klaar") 