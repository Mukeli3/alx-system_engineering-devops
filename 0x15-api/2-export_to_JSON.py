#!/usr/bin/python3
"""
export data in the JSON format
"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    first_url = f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
    usrResponse = requests.get(first_url)

    nm = usrResponse.json().get("name")
    second_url = f"https://jsonplaceholder.typicode.com/users/{argv[1]}/todos"

    tdsResponse = requests.get(second_url)
    todos = tdsResponse.json()

    todoList = [{'task': task['title'],
                 'completed': task['completed'],
                 'username': nm}
                for task in todos]

    todoDict = {argv[1]: todoList}

    with open(argv[1] + ".json", 'w') as j_file:
        json.dump(todoDict, j_file)
