def voeg__toe(telefoonboek, naam, nummer):
    "Return het boek, met naam & nummer erbij"
    telefoonboek.append([naam, nummer])
    return telefoonboek

telefoonboek = [
    ["Jan Janssen", "+32 470 998301"],
    ["Piet Joris", "+32 483 313220"],
    ["Kor Neel", "+32 453 231456"],
    ["Piet Dirkx", "+31 269 542463"]
]

telefoonboek = voeg__toe(telefoonboek, "Jos", 123)

print(telefoonboek)

