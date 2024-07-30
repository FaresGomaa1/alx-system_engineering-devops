#!/usr/bin/python3

import requests
import sys


def gather_data(employee_id):
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(url)

    if user_response.status_code != 200:
        print(f"Error: User with ID {employee_id} not found.")
        return

    user_data = user_response.json()
    user_name = user_data.get("name")

    todos_url = (f"https://jsonplaceholder.typicode.com/users/"
                 f"{employee_id}/todos")
    todos_response = requests.get(todos_url)

    if todos_response.status_code != 200:
        print("Error: Unable to fetch TODOs.")
        return

    todos_data = todos_response.json()
    total_tasks = len(todos_data)
    completed_tasks = [
        task["title"] for task in todos_data if task["completed"]
    ]
    number_of_done_tasks = len(completed_tasks)

    # Print results
    print(f"Employee {user_name} is done with tasks("
          f"{number_of_done_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)

    gather_data(employee_id)
