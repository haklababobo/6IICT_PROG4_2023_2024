"""
Vul dit bestand aan met de instructies in OneNote.
"""
class Account:
    def __init__(self, naam, balans, type):
        self.naam = naam
        self.balans = balans
        self.type = type

#   def __str__(self):
#       return (f"Account van {self.naam} met een balans van {self.balans} {self.type}")

## Kleine test van gebruik van de klasse.
# if __name__ == "__main__":
#     account1 = Account("Jan", 1000, "EUR")
#     account2 = Account("Piet", 2000, "EUR")
    
#     print(account1)
#     print(account2)

class Bank:
    def __init__(self, naam, bonus):
        self.naam = naam
        self.accounts = []
        self.bonus = bonus

    def toevoegen(self, account):
        if isinstance(account, Account):
            self.accounts.append(account)
            print(f"Account van {account.naam} toegevoegd.")
        else:
            print("Geen geldig account opgegeven.")

    def overzicht(self):
        print(f"Bank {self.naam} heeft volgende accounts:")
        for account in self.accounts:
            account.overzicht()

    def bonus_uitkeren(self):
        for account in self.accounts:
            if account.type == "basis":
                account.stort(self.bonus)
            elif account.type == "premium":
                account.stort(self.bonus * 2)


    def overzicht(self):
        print(f"{self.naam} ({self.type}): {self.balans} euro.")

    def stort(self, bedrag):
        if isinstance(bedrag, (int, float)):
            self.balans += bedrag
            print(f"Nieuwe balans: {self.balans} euro.")
        else:
            print("Ongeldig bedrag ontvangen.")

    def afhalen(self, bedrag):
        if isinstance(bedrag, (int, float)):
            if self.balans - bedrag >= 0:
                self.balans -= bedrag
                print(f"Nieuwe balans: {self.balans} euro.")
            else:
                print("Ontoereikende balans.")
        else:
            print("Ongeldig bedrag ontvangen.")

# Voorbeeld van het gebruik van de Account-klasse
# if __name__ == "__main__":
#     account1 = Account("Jan", 1000, "EUR")
#     account2 = Account("Piet", 2000, "EUR")

#     account1.overzicht()
#     account1.stort(500)
#     account1.afhalen(2000)

#     account2.overzicht()
#     account2.afhalen(3000)
