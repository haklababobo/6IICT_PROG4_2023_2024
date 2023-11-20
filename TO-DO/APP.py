import requests
import os
import subprocess

def create_project(project_name):
    command1 = subprocess.run('uuidgen', shell=True, capture_output=True, text=True).stdout

    headers = {
        'Content-Type': 'application/json',
        'X-Request-Id': command1,
        'Authorization': '1cffd55a56d01ac4a2cbf67e8996d5b7c9a28127',
    }
    json_data = {
        'name': project_name,
    }

    response = requests.post('https://api.todoist.com/rest/v2/projects', headers=headers, json=json_data)

    if response.status_code == 200:
        print("Project created successfully.")
    else:
        print("Error creating project:", response.status_code, response.text)

def create_task(api_token, content, project_id):
    command2 = subprocess.run('uuidgen', shell=True, capture_output=True, text=True).stdout

    headers = {
        'Content-Type': 'application/json',
        'X-Request-Id': command2,  # Use a different UUID for tasks
        'Authorization': '1cffd55a56d01ac4a2cbf67e8996d5b7c9a28127',
    }
    json_data = {
        'content': content,
        'project_id': project_id,
    }
    response = requests.post('https://api.todoist.com/rest/v2/tasks', headers=headers, json=json_data)

    if response.status_code == 200:
        print("Task created successfully.")
    else:
        print("Error creating task:", response.status_code, response.text)

def list_tasks(api_token):
    headers = {
        'Authorization': '1cffd55a56d01ac4a2cbf67e8996d5b7c9a28127',
    }
    response = requests.get('https://api.todoist.com/rest/v2/tasks', headers=headers)

    if response.status_code == 200:
        tasks = response.json()
        print("Tasks:")
        for task in tasks:
            print(task)
    else:
        print("Error fetching tasks:", response.status_code, response.text)

print("keuzemenu")
print("keuze een is post_project")
print("keuze twee is post_task")
print("keuze drie is get_task")

while True:
    keuze = input("geef een cijfer in: ")

    if keuze == "1":
        api_token = '1cffd55a56d01ac4a2cbf67e8996d5b7c9a28127'  # Replace with your actual Todoist API token
        project_name = input("Enter project name: ")
        create_project(api_token, project_name)

    elif keuze == "2":
        api_token = '1cffd55a56d01ac4a2cbf67e8996d5b7c9a28127'  # Replace with your actual Todoist API token
        content = input("Enter task content: ")
        project_id = '2321375405'  # Replace with the correct project_id
        create_task(api_token, content, project_id)

    elif keuze == "3":
        api_token = '1cffd55a56d01ac4a2cbf67e8996d5b7c9a28127'  # Replace with your actual Todoist API token
        list_tasks(api_token)
