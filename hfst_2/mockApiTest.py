import requests, json

# Haal alle blogs op
url = "https://6575b939b2fbb8f6509d6d17.mockapi.io/api/blog"

response = requests.get(url)
response_json = response.json()

print("Alle blogs: ", response_json)
print("\n" +  "#" * 80 + "\n")

# Haal een specifieke blog op
url = "https://6575b939b2fbb8f6509d6d17.mockapi.io/api/blog/1"

response = requests.get(url)
response_json = response.json()

print("Een specifieke blog: ", response_json)
print("\n" +  "#" * 80 + "\n")

# Maak een nieuwe blog aan
url = "https://6575b939b2fbb8f6509d6d17.mockapi.io/api/blog"

blog = {
    "id": 22,
    "title": "title 22",
    "text": "text 22",
    "createdAt": 1702213033,
    "updatedAt": 1702213033,
    "author": "author 22"
}

blogs = requests.get(url)
blogs_json = blogs.json()

for bl in blogs_json:
    if blog["id"] == bl["id"]: 
        print("Blog met ID: " + bl["id"] + " BESTAAT AL !!! ")
        pass
    else:
        bl
        pass

response = requests.post(url, blog)
print("Blog is succesvol toegevoegd: ", response)
print("\n" +  "#" * 80 + "\n")

# Pas een bestaande blog aan
url = "https://6575b939b2fbb8f6509d6d17.mockapi.io/api/blog/22"

blog = {
    "id": 22,
    "title": "title 22",
    "text": "text 22",
    "createdAt": 1702213044,
    "updatedAt": 1702213044,
    "author": "author 22"
}

response = requests.put(url, blog)

print("Blog is succesvol aangepast: ", response)
print("\n" +  "#" * 80 + "\n")

# Verwijder een bestaande blog
# url = "https://6575b939b2fbb8f6509d6d17.mockapi.io/api/blog/23"

# response = requests.delete(url)

# print("Blog is succesvol verwijderd: ", response)
# print("\n" +  "#" * 80 + "\n")