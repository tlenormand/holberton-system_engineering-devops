#!/usr/bin/python3
''' export to csv '''
import requests
import sys
import csv


if __name__ == "__main__":
    userRequest = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}"
    )
    userName = userRequest.json()["username"]
    userId = userRequest.json()["id"]
    response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}/todos"
    )
    json = response.json()

    todoList = []

    f = open(f'{userId}.csv', 'w')
    writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    for idx in json:
        writer.writerow([userId, userName, idx["completed"], idx["title"]])
    f.close()
