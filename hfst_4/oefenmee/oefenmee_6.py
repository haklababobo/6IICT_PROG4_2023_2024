try:
    fruit_lijst = ["Appel", "Banaan", "Meloen", "Mango", "Druif"]
    getal = int( input("Hoeveel fruit uit de lijst wil je printen: ") )

    for i in range(getal):
        fruit = fruit_lijst[i]
        print(fruit)
except IndexError:
    print("te hoog getal voor de lijst")
except ValueError:
    print("Je kan enkel getallen ingeven")