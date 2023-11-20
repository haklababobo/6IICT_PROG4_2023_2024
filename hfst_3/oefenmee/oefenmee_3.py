"""
Maak de app na volgens de foto bij oefen mee 3.
Je hebt maar 3 labels nodig om deze app te maken.
"""
import tkinter as tk

app = tk.Tk()

# Maak labels voor de woorden
labels = ["hallo", "klas", "6IICT"]

# Loop door de labels en plaats ze in het raster
for i, word in enumerate(labels):
    # Bepaal de rij en kolom op basis van de index
    row = i // 2  # Integerdeling om rijen te verdelen
    col = i % 2   # Modulus om kolommen te verdelen

    label = tk.Label(master=app, text=word)
    label.grid(row=row, column=col)

app.mainloop()
