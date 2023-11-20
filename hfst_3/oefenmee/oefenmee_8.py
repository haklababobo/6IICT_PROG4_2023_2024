"""
Volg de instructies van oefen mee 8.
Je zal een simpel rekenmachine maken met behulp van 2 Entries, 1 label & 1 button.
    
    Tip! De methode .get() van entries geeft altijd een string.
         Je kan hier natuurlijk niet mee rekenen.
"""
import tkinter as tk

# Functie voor het uitvoeren van berekeningen
def bereken():
    getal1 = entry1.get()
    getal2 = entry2.get()

    try:
        resultaat = float(getal1) + float(getal2)
        label.config(text=f"Resultaat: {resultaat}")
    except ValueError:
        label.config(text="Ongeldige invoer")

# Maak een GUI-venster
venster = tk.Tk()
venster.title("Rekenmachine")

# Voeg twee invoervelden (Entries) toe met grid
entry1 = tk.Entry(venster)
entry2 = tk.Entry(venster)

entry1.grid(row=0, column=0)
entry2.grid(row=0, column=1)

# Voeg een label toe om het resultaat weer te geven met grid
label = tk.Label(venster, text="Resultaat: ")
label.grid(row=1, column=0, columnspan=2)

# Voeg een knop toe om de berekening uit te voeren
bereken_knop = tk.Button(venster, text="Bereken", command=bereken)
bereken_knop.grid(row=2, column=0, columnspan=2)

# Start de GUI-loop
venster.mainloop()