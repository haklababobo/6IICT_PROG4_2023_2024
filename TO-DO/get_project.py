import requests

headers = {
    'Authorization': 'Bearer 1cffd55a56d01ac4a2cbf67e8996d5b7c9a28127',
}

response = requests.get('https://api.todoist.com/rest/v2/projects', headers=headers).json()

print(response)