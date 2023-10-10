import subprocess
import requests

command1 = subprocess.run('uuidgen', shell=True, capture_output=True, text=True).stdout

headers = {
    'X-Request-Id': command1,
    'Authorization': 'Bearer 0123456789abcdef0123456789',
}

response = requests.delete('https://api.todoist.com/rest/v2/projects/2203306141', headers=headers)