# Werk verder met de klasse Hond van oefen mee 1.
class Hond:
    def weegschaal(self, naam, massa):
        self.naam = naam
        self.massa = massa

    def blaf(self):
        print(f"{self.naam} zegt blaf.")

# Maak twee objecten van de klasse Hond
mijn_hond1 = Hond()
mijn_hond2 = Hond()

# Roep de blaf-methode aan voor beide honden
mijn_hond1.weegschaal('bonny', 8)
mijn_hond2.weegschaal('babs', 6)

mijn_hond1.blaf()
mijn_hond2.blaf()

print("Naam van de hond:", mijn_hond1.naam)
print("Massa van de hond:", mijn_hond1.massa)
print("Naam van de hond:", mijn_hond2.naam)
print("Massa van de hond:", mijn_hond2.massa)