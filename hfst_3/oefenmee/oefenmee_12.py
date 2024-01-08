import tkinter as tk

def knop_nummer_ingedrukt(nummer):
    def inner():
        veld.insert(tk.END, str(nummer))
    return inner

def plus_ingedrukt():
    global getal_1, operator
    operator = "+"
    getal_1 = float(veld.get())
    veld.delete(0, tk.END)

def min_ingedrukt():
    global getal_1, operator
    operator = "-"
    getal_1 = float(veld.get())
    veld.delete(0, tk.END)

def isgelijk_ingedrukt():
    getal_2 = float(veld.get())
    veld.delete(0, tk.END)
    if operator == "+":
        resultaat = getal_1 + getal_2
    elif operator == "-":
        resultaat = getal_1 - getal_2
    else:
        resultaat = "Error"
    veld.insert(tk.END, str(resultaat))

def clr_ingedrukt():
    global getal_1, getal_2, operator
    getal_1 = 0
    getal_2 = 0
    operator = ""
    veld.delete(0, tk.END)

app = tk.Tk()

app.resizable(width=False, height=False)

settings = {
    "master": app, "width": 6, "height": 2, "borderwidth": 3,
    "highlightthickness": 2, "highlightbackground": "black"
}

veld = tk.Entry(master=app, background="lime", borderwidth=3)
veld.grid(row=0, column=0, columnspan=3)

knop_nummers = [tk.Button(**settings, text=str(i), command=knop_nummer_ingedrukt(i)) for i in range(10)]
knop_nummers[0].grid(row=4, column=0)
for i in range(1, 10):
    knop_nummers[i].grid(row=(i - 1) // 3 + 1, column=(i - 1) % 3)

knop_plus = tk.Button(**settings, text="+", command=plus_ingedrukt)
knop_plus.grid(row=4, column=1)
knop_min = tk.Button(**settings, text="-", command=min_ingedrukt)
knop_min.grid(row=4, column=2)

knop_isgelijk = tk.Button(**settings, text="=", command=isgelijk_ingedrukt)
knop_isgelijk.grid(row=5, column=0)
knop_clr = tk.Button(font=("Calibri", 15), text="clr", width=10, height=1, command=clr_ingedrukt)
knop_clr.grid(row=5, column=1, columnspan=2, pady=10)

getal_1 = 0
getal_2 = 0
operator = ""

app.mainloop()