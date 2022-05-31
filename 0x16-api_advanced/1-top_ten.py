#!/usr/bin/python3
"""
queries the Reddit API and prints the titles of the first 10 hot posts
"""
import requests


def top_ten(subreddit):
    """
    queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit
    """
    response = requests.get(
        "https://www.reddit.com/r/" + subreddit + "/hot.json",
        headers={'User-Agent': 'Holberton'}
    )

    if response.status_code == 404:
        print("None")
    else:
        data = response.json()["data"]["children"]
        for title in data[:10]:
            print(title["data"]["title"])
