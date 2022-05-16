#!/usr/bin/python3
''' api fetch '''
import requests
import sys


if __name__ == "__main__":
    userNameRequest = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}"
    )
    userName = userNameRequest.json()["username"]
    response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}/todos"
    )
    json = response.json()

    i = 0
    todoList = []
    did = 0
    total = 0

    for idx in json:
        if idx["completed"]:
            todoList.append(idx["title"])
            did += 1
        total += 1

    print(f"Employee {userName} Howell is done with tasks({did}/{total}):")
    for idx in todoList:
        print("\t" + idx)
