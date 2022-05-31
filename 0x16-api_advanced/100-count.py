#!/usr/bin/python3

"""
Python file 0x16 - API Advenced
"""

import requests


def count_words(subreddit, word_list, dictWord={}, after=None):
    """
    Recursive function that queries the Reddit API, parses the title
    of all hot articles, and prints a sorted count of given keywords
    (case-insensitive, delimited by spaces. Javascript should count as
    javascript, but java should not)
    """
    if subreddit is None:
        print(None)
    URL = 'http://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {
        'User-Agent': 'Holberton User Agent 1.0',
        'From': 'mickael.boillaud@gmail.com',
    }
    response = requests.get(
        URL,
        headers=headers,
        params={'after': after, 'limit': 10}
    )
    if response.status_code == 404:
        return
    data = response.json()
    allHot = data.get("data", {}).get("children", None)
    after = data.get("data", {}).get("after", None)
    for hotPost in allHot:
        title = hotPost.get("data", {}).get("title", "").lower().split()
        for word in word_list:
            if word.lower() in title:
                totalIteration = 0
                for w in title:
                    if word.lower() == w:
                        totalIteration += 1
                if word.lower() not in dictWord.keys():
                    dictWord[word.lower()] = totalIteration
                else:
                    dictWord[word.lower()] += totalIteration
    if after is None:
        if len(dictWord) == 0:
            pass
        else:
            dictWord = sorted(dictWord.items(), key=lambda kv: (-kv[1], kv[0]))
            for key, value in dictWord:
                print('{}: {}'.format(key, value))
        return
    return count_words(subreddit, word_list, dictWord, after)
  
