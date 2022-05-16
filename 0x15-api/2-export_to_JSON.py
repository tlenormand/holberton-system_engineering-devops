#!/usr/bin/python3
''' export to json '''
import requests
import sys
import json


if __name__ == "__main__":
    userRequest = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}"
    )
    userName = userRequest.json()["username"]
    userId = userRequest.json()["id"]
    response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}/todos"
    )
    jsonResponse = response.json()

    userDict = {userId: []}

    for idx in jsonResponse:
        userDict[userId].append({
            "task": idx["title"],
            "completed": idx["completed"],
            "username": userName,
        })

    f = open(f'{userId}.json', 'w')
    json.dump(userDict, f)
    f.close()
