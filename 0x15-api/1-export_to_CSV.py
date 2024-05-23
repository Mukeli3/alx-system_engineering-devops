#!/usr/bin/python3
"""
export data in the CSV format
"""

import csv
import requests
from sys import argv


if __name__ == "__main__":
    first_url = f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
    usrResponse = requests.get(first_url)

    nm = usrResponse.json().get("name")
    second_url = f"https://jsonplaceholder.typicode.com/users/{argv[1]}/todos"

    tdsResponse = requests.get(second_url)
    todos = tdsResponse.json()

    with open(argv[1] + ".csv", 'w', newline="") as file:
        wrter = csv.writer(file, quoting=csv.QUOTE_ALL)
        [wrter.writerow(
            [argv[1], nm, str(task['completed']), task['title']])
            for task in todos]
