""" 
Maak een app aan die 3 labels bevat.
De inhoud van de 3 labels is:
    - Label 1: hallo
    - Label 2: klas
    - Label 3: 6iict
"""

import tkinter as tk

# Maak een nieuwe applicatie
app = tk.Tk()
app.title("Mijn App")

# Voeg drie labels toe aan de app
label1 = tk.Label(app, text="Hallo")
label1.pack()

label2 = tk.Label(app, text="Klas")
label2.pack()

label3 = tk.Label(app, text="6IICT")
label3.pack()

# Start de app
app.mainloop()
