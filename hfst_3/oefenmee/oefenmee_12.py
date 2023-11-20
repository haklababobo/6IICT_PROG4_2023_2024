"""
Volg de instructies van oefen mee 12.
In deel 1 van de oefen mee maak je het uiterlijk van een rekenmachine.
In deel 2 zal je deze ook echt laten werken.

    Tip! Je kan instellingen van widgets ook inladen via een dictionary.
         Op deze manier kan je veel gelijkaardige widgets snel opstellen en aanpassen.
         Er is een voorbeeld onderaan de oefen mee voorzien.
"""
import tkinter as tk
app = tk.Tk()

app.resizable (width= False, height= False)

settings = {
    "master": app, "width" : 6, "height" : 2, "borderwidth" : 3, 
    "highlightthickness": 2,"highlightbackground": "black"
}

veld = tk.Entry(master=app, background="lime", borderwidth= 3)
veld.grid(row=0 , column = 0, columnspan = 3)

knop1 = tk.Button(**settings, text="1")
knop1.grid(row=1, column=0)
knop2 = tk.Button(**settings, text="2")
knop2.grid(row=1,column=1)
knop3 = tk.Button(**settings, text="3")
knop3.grid(row=1,column=2)

knop4 = tk.Button(**settings, text="4")
knop4.grid(row=2, column=0)
knop5 = tk.Button(**settings, text="5")
knop5.grid(row=2,column=1)
knop6 = tk.Button(**settings, text="6")
knop6.grid(row=2,column=2)

knop7 = tk.Button(**settings, text="7")
knop7.grid(row=3, column=0)
knop8 = tk.Button(**settings, text="8")
knop8.grid(row=3,column=1)
knop9 = tk.Button(**settings, text="9")
knop9.grid(row=3,column=2)

knop10 = tk.Button(**settings, text="0")
knop10.grid(row=4, column=0)
knop11 = tk.Button(**settings, text="+")
knop11.grid(row=4,column=1)
knop12 = tk.Button(**settings, text="-")
knop12.grid(row=4,column=2)

knop13 = tk.Button(**settings, text= "=")
knop13.grid(row=5,column=0)
knop14 = tk.Button(font=("Calibri", 15), text= "clr", width=10, height=1)
knop14.grid(row=5,column=1, columnspan=2, pady=10)


app.mainloop()
