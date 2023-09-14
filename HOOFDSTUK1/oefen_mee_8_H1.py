steden_temp = {
    "Hasselt": 25,
    "Oostende": 21,
    "Antwerpen": 24,
    "Brussel": 23,
    "Luik": 23,
    "Namen": 24
}

# Vraag de gebruiker om een stad
stad = input("In welke stad bent u: ")

# Gebruik de get() methode om de temperatuur op te halen of 22 als de stad niet bestaat
temp = steden_temp.get(stad, 22)

# Print het resultaat
if temp == 22:
    print(f"{stad} bestaat niet. Het is in België {temp}°C.")
else:
    print(f"Het is {temp}°C.")
