import os
import requests

headers = {
    'Authorization': 'Bearer ' + os.getenv('token', '1cffd55a56d01ac4a2cbf67e8996d5b7c9a28127'),
}

response = requests.get('https://api.todoist.com/rest/v2/tasks', headers=headers).json()

print(response)