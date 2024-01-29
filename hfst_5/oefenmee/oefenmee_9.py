import random

class Hond:
    locaties = ["living", "tuin", "buren", "keuken"]

    def __init__(self, naam):
        self.naam = naam
        self.locatie = random.choice(self.locaties)
        print(f"{self.naam} zit willekeurig in de {self.locatie}.")

    def ziet_hond(self, andere_hond):
        if self.locatie == andere_hond.locatie:
            print(f"{self.naam} ziet {andere_hond.naam} in de {self.locatie}.")

            # Hond wordt bang en rent naar een nieuwe locatie
            nieuwe_locatie = random.choice([locatie for locatie in self.locaties if locatie != self.locatie])
            print(f"{self.naam} is bang en rent naar de {nieuwe_locatie}.")
            self.locatie = nieuwe_locatie

        else:
            print(f"{self.naam} ziet {andere_hond.naam} niet in de {self.locatie}.")

# Voorbeeldgebruik:
hond_1 = Hond("Lulu")
hond_2 = Hond("Floris")
hond_3 = Hond("Ranger")

hond_1.ziet_hond(hond_2)
hond_1.ziet_hond(hond_3)

print(hond_1.locatie)
