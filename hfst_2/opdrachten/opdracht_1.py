import requests

def main():
    print("Welkom bij de JokeAPI-terminal-app!")
    category = input("Geef een categorie van grap in (alle, programmeren, kerst, enz.): ")
    
    # Stuur een verzoek naar de JokeAPI
    url = f"https://v2.jokeapi.dev/joke/{category}"
    response = requests.get(url)
    
    if response.status_code == 200:
        joke_data = response.json()
        if joke_data['type'] == 'single':
            print("Hier is een eendelige grap:")
            print(joke_data['joke'])
        elif joke_data['type'] == 'twopart':
            print("Hier is een tweedelige grap:")
            print("Vraag:", joke_data['setup'])
            print("Antwoord:", joke_data['delivery'])
        else:
            print("Onbekend graptype")
    else:
        print("Er is een fout opgetreden bij het ophalen van de grap.")
    
    # Wacht tot de gebruiker op ENTER drukt om af te sluiten
    input("Druk op ENTER om af te sluiten.")

if __name__ == "__main__":
    main()
