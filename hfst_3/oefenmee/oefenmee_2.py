"""
VOER DE CODE NOG NIET UIT!
"""
import tkinter as tk

app = tk.Tk()

# Label 1 op rij 1
label_1 = tk.Label(master=app, text="Label 1")
label_1.grid(row=1, column=0)

# Lege label op rij 2
label_empty_2 = tk.Label(master=app, text="")
label_empty_2.grid(row=2, column=0)

# Label 3 op rij 3
label_3 = tk.Label(master=app, text="Label 3")
label_3.grid(row=3, column=0)

# Lege label op rij 4
label_empty_4 = tk.Label(master=app, text="")
label_empty_4.grid(row=4, column=0)

# Label 5 op rij 5
label_5 = tk.Label(master=app, text="Label 5")
label_5.grid(row=5, column=0)

app.mainloop()

