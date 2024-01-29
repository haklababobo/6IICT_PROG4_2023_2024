# Maak de klasse Persoon & Hond aan zoals omschreven in oefen mee 10.
# Je start reeds met de __init__ van beide klassen.

class Hond:
    def __init__(self, naam):
        self.naam = naam
        self.eigenaar = ""

class Persoon:
    def __init__(self, naam):
        self.naam = naam
        self.honden = []

    def koop_hond(self, hond):
        if hond.eigenaar == "":
            self.honden.append(hond.naam)
            hond.eigenaar = self.naam
        else:
            print(f"{hond.naam} heeft reeds {hond.eigenaar} als eigenaar.")

    def is_eigenaar(self, hond):
        return hond.eigenaar == self.naam


# Testcode voor Niveau 1
hond_1 = Hond("Lulu")
hond_2 = Hond("Floris")
persoon_1 = Persoon("Jos")
persoon_2 = Persoon("Jef")

persoon_1.koop_hond(hond_1)
persoon_2.koop_hond(hond_2)

print(persoon_1.is_eigenaar(hond_1))
print(persoon_2.is_eigenaar(hond_1))


# Testcode voor Niveau 2
hond_1 = Hond("Lulu")
hond_2 = Hond("Floris")
persoon_1 = Persoon("Jos")
persoon_2 = Persoon("Jef")

persoon_1.koop_hond(hond_1)
persoon_2.koop_hond(hond_2)
persoon_2.koop_hond(hond_1)

print(persoon_1.is_eigenaar(hond_1))
print(persoon_2.is_eigenaar(hond_1)) 
