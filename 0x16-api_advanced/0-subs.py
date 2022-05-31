#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    queries the Reddit API

    Returns:
        number of subscribers
        0 if invalid subreddit given
    """
    response = requests.get(
        "https://www.reddit.com/r/" + subreddit + "/about.json",
        headers={'User-Agent': 'Holberton'}
    )

    if response.status_code == 404:
        return 0

    return response.json()["data"]["subscribers"]
