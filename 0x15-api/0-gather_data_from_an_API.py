#!/usr/bin/python3
"""
Script returns information about employee's TODO list progress
given his/her ID using REST API
"""

import requests
from sys import argv


if __name__ == "__main__":
    first_url = f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
    usrResponse = requests.get(first_url)

    nm = usrResponse.json().get("name")
    second_url = f"https://jsonplaceholder.typicode.com/users/{argv[1]}/todos"

    tdsResponse = requests.get(second_url)
    todos = tdsResponse.json()
    allTodos = len(todos)
    completed = sum(task['completed'] for task in todos)

    print(f"Employee {nm} is done with tasks({completed}/{allTodos}):")

    for task in todos:
        if task['completed']:
            print(f"\t {task['title']}")
