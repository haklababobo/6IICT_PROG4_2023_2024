# Bepaal de faculteit van een getal met behulp van een while-loop.
def facul(getal):
    resultaat = 1
    while getal > 1:
        resultaat *= getal
        getal -= 1
    return resultaat


print( facul(1) ) # 1
print( facul(2) ) # 2
print( facul(3) ) # 6
print( facul(4) ) # 24
print( facul(5) ) # 120