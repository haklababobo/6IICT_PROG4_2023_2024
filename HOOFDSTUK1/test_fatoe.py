import requests

url = "https://v2.jokeapi.dev/joke/Any?" 

response = requests.get(url) 

print(response.json()) # <Response [200]> 