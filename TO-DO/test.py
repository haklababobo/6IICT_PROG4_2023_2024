import requests
import json

# Set your Todoist API token
api_token = "1cffd55a56d01ac4a2cbf67e8996d5b7c9a28127"

# Define the base URL for the Todoist API
base_url = "https://api.todoist.com/rest/v2"

# Create a new project
def create_project():
    project_name = input("Enter project name: ")
    data = {"name": project_name}
    response = requests.post(f"{base_url}/projects", headers={"Authorization": f"Bearer {api_token}"}, json=data)
    return response.json()

# Get all projects
def get_projects():
    response = requests.get(f"{base_url}/projects", headers={"Authorization": f"Bearer {api_token}"})
    return response.json()

# Create a new task in a project
def create_task(project_id):
    task_name = input("Enter task name: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    data = {
        "content": task_name,
        "due_string": due_date,
        "project_id": project_id
    }
    response = requests.post(f"{base_url}/tasks", headers={"Authorization": f"Bearer {api_token}"}, json=data)
    return response.json()

# Get tasks in a project
def get_tasks(project_id):
    response = requests.get(f"{base_url}/tasks", headers={"Authorization": f"Bearer {api_token}"}, params={"project_id": project_id})
    return response.json()

# Update a task
def update_task(task_id):
    new_content = input("Enter new task content: ")
    data = {"content": new_content}
    response = requests.post(f"{base_url}/tasks/{task_id}", headers={"Authorization": f"Bearer {api_token}"}, json=data)
    return response.json()

# Delete a task
def delete_task(task_id):
    response = requests.delete(f"{base_url}/tasks/{task_id}", headers={"Authorization": f"Bearer {api_token}"})
    return response.json()

if __name__ == "__main__":
    while True:
        print("1. Create a new project")
        print("2. List all projects")
        print("3. Create a new task in a project")
        print("4. List tasks in a project")
        print("5. Update a task")
        print("6. Delete a task")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            project = create_project()
            print(f"Created project: {project['name']} (ID: {project['id']})")
        elif choice == "2":
            projects = get_projects()
            for project in projects:
                print(f"{project['name']} (ID: {project['id']})")
        elif choice == "3":
            projects = get_projects()
            if not projects:
                print("No projects available. Create a project first.")
            else:
                project_id = input("Enter project ID for the new task: ")
                task = create_task(int(project_id))
                print(f"Created task: {task['content']} (ID: {task['id']})")
        elif choice == "4":
            project_id = input("Enter project ID to list tasks: ")
            tasks = get_tasks(int(project_id))
            for task in tasks:
                print(f"{task['content']} (ID: {task['id']})")
        elif choice == "5":
            task_id = input("Enter task ID to update: ")
            response = update_task(int(task_id))
            print(f"Task updated: {response['content']}")
        elif choice == "6":
            task_id = input("Enter task ID to delete: ")
            response = delete_task(int(task_id))
            if 'error' in response:
                print(f"Error: {response['error']['message']}")
            else:
                print("Task deleted successfully.")
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")