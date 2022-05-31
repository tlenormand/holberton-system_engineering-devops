#!/usr/bin/python3
"""
queries the Reddit API
"""
import requests


def add_value(hot_list, data, count=0):
    """
    add value recursively in list
    """
    try:
        hot_list.append(data["children"][count]["data"]["title"])
    except IndexError:
        return hot_list
    count += 1

    return add_value(hot_list, data, count)


def recurse(subreddit, hot_list=[], after=None):
    """
    queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit

    Returns:
        list containing the titles of all hot articles
        None if no result found
    """
    response = requests.get(
        "https://www.reddit.com/r/" + subreddit + "/hot.json",
        headers={'User-Agent': 'Holberton'},
        params={'after': after}
    )

    if response.status_code == 404:
        return None

    data = response.json()["data"]
    hot_list = add_value(hot_list, data)
    if data["after"] is None:
        return hot_list

    return recurse(subreddit, hot_list, data["after"])
