# Los de vragen uit oefen mee 2 op.

def optellen(getal):
    if getal == 1:
        print(getal)
        return
    
    print(getal)
    optellen(getal+1)

    

optellen(3)