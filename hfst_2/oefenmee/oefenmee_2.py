import requests

url = "https://v2.jokeapi.dev/joke/Any?"
response = requests.get(url)

print(response)        # <Response [200]>
print(response.json()) # Data in JSON-formaat
print("#" * 40)       # Scheiding in opdrachtprompt

response_json = response.json()

# Controleer of de sleutels "setup" en "delivery" aanwezig zijn
if "setup" in response_json and "delivery" in response_json:
    print(response_json["setup"])    # De setup
    print(response_json["delivery"]) # De punchline
else:
    print("De JSON bevat geen setup en delivery voor deze grap.")
