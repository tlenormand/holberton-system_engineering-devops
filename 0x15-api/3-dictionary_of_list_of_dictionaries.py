#!/usr/bin/python3
# api fetch
import requests
import sys
import json


if __name__ == "__main__":

    userNameRequest = requests.get(
        f"https://jsonplaceholder.typicode.com/users"
    )
    users = userNameRequest.json()

    dataDict = {}

    for user in users:
        userId = user["id"]
        response = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{userId}/todos"
        )
        todos = response.json()

        dataDict[str(user["id"])] = []
        for todo in todos:
            dataDict[str(user["id"])].append({
                "username": user["username"],
                "task": todo["title"],
                "completed": todo["completed"]
            })

    f = open(f'todo_all_employees.json', 'w')
    json.dump(dataDict, f)
    f.close()
