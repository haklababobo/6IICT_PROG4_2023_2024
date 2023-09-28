import requests

url = "https://v2.jokeapi.dev/joke/Christmas?amount=3"
response_json = requests.get(url).json()

# Controleer of de respons een lijst van grappen bevat
if "jokes" in response_json:
    jokes = response_json["jokes"]
    
    # Loop door de lijst met grappen en print ze
    for i, joke in enumerate(jokes, start=1):
        print(f"Grap {i}...")
        if "joke" in joke:
            print(joke["joke"])
        else:
            print(joke["setup"])
            print(joke["delivery"])
        print()
else:
    print("Geen grappen gevonden in de respons.")
