import subprocess
import requests

command1 = subprocess.run('uuidgen', shell=True, capture_output=True, text=True).stdout

headers = {
    # Already added when you pass json=
    # 'Content-Type': 'application/json',
    'X-Request-Id': command1,
    'Authorization': 'Bearer 1cffd55a56d01ac4a2cbf67e8996d5b7c9a28127',
}

json_data = {
    'name': 'Shopping List',
}

response = requests.post('https://api.todoist.com/rest/v2/projects', headers=headers, json=json_data).json()

print(response)