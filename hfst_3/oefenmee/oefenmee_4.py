"""
Maak de app na volgens de foto bij oefen mee 3.
Je zal de parameters columnspan & rowspan van .grid() moeten gebruiken.
"""
import tkinter as tk

app = tk.Tk()

# Eerste rij
label_1 = tk.Label(app, text="Label 1")
label_1.grid(row=0, column=0, columnspan=2)  # Neemt 2 kolommen in beslag

label_2 = tk.Label(app, text="Label 2")
label_2.grid(row=0, column=2, columnspan=2)  # Neemt 2 kolommen in beslag

# Tweede rij
label_3 = tk.Label(app, text="Label 3")
label_3.grid(row=1, column=0, rowspan=2)  # Neemt 2 rijen in beslag

label_4 = tk.Label(app, text="Label 4")
label_4.grid(row=1, column=1)

label_5 = tk.Label(app, text="Label 5")
label_5.grid(row=2, column=1)

# Derde rij
label_6 = tk.Label(app, text="Label 6")
label_6.grid(row=3, column=0, columnspan=2)  # Neemt 2 kolommen in beslag

label_7 = tk.Label(app, text="Label 7")
label_7.grid(row=3, column=2, columnspan=2)  # Neemt 2 kolommen in beslag

app.mainloop()
