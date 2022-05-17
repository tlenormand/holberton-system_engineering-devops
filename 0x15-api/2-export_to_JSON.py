#!/usr/bin/python3
''' export to json '''
import json
import requests
import sys


if __name__ == "__main__":
    userRequest = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(
            sys.argv[1]
        )
    )
    userName = userRequest.json()["username"]
    userId = userRequest.json()["id"]
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos".format(
            sys.argv[1]
        )
    )
    jsonResponse = response.json()

    userDict = {userId: []}

    for idx in jsonResponse:
        userDict[userId].append({
            "task": idx["title"],
            "completed": idx["completed"],
            "username": userName,
        })

    f = open('{}.json'.format(userId), 'w')
    json.dump(userDict, f)
    f.close()
