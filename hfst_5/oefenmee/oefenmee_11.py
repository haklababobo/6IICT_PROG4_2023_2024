class Dier:
    def __init__(self, naam, leeftijd):
        self.naam = naam
        self.leeftijd = leeftijd

    def heeft_naam(self):
        print(f"Dit dier heeft de naam {self.naam}.")

class Hond(Dier):
    def __init__(self, naam, leeftijd):
        super().__init__(naam, leeftijd)

    def kind(self):
        print(f'Deze hond heeft een jong.')

hond_1 = Hond("Boris", 9)
print(f"{hond_1.naam} heeft {hond_1.leeftijd} jaar oud.")

class Kat(Dier):
    pass

kat_1 = Kat("Fluffy", 5)
kat_1.heeft_naam()
