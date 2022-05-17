#!/usr/bin/python3
''' export data in the JSON format '''
import requests
import sys
import json


if __name__ == "__main__":

    userNameRequest = requests.get(
        "https://jsonplaceholder.typicode.com/users"
    )
    users = userNameRequest.json()

    dataDict = {}

    for user in users:
        userId = user["id"]
        response = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}/todos".format(
                userId
            )
        )
        todos = response.json()

        dataDict[str(user["id"])] = []
        for todo in todos:
            dataDict[str(user["id"])].append({
                "username": user["username"],
                "task": todo["title"],
                "completed": todo["completed"]
            })

    f = open('todo_all_employees.json', 'w')
    json.dump(dataDict, f)
    f.close()
