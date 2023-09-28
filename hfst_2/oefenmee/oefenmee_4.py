import requests
import json

url = "https://api.adviceslip.com/advice/search/api"
response_json = requests.get(url).json()

# De volledige padnaam van het bestand
bestand_pad = "hfst_2/oefenmee/bericht_adviceslip.json"

# Het JSON-antwoord opslaan in het bestand
with open(bestand_pad, "w") as bestand:
    json.dump(response_json, bestand, indent=4)

print(f"De JSON-respons is opgeslagen in {bestand_pad}")
