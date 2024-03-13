# Niveau 1: bepaal sommatie van een getal recursief.

def sommatie(getal):
    if getal == 1:
        return 1
   
    vorige_sommato = sommatie( getal-1 )
    return  getal + vorige_sommato

# niveau 2: bepaal sommatie van een getal met while-loop.

def sommatie(getal):
 
    uitkomst = 0
    while getal > 0:
        uitkomst = uitkomst + getal
        getal = getal - 1
 
    return uitkomst


print( sommatie(1) )   # 1
print( sommatie(2) )   # 3
print( sommatie(3) )   # 6
print( sommatie(4) )   # 10
print( sommatie(5) )   # 15
print( sommatie(100) ) # 5050
