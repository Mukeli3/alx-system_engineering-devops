#!/usr/bin/python3
"""
Contains def number_of_subscribers(subreddit) function
"""
import requests


def number_of_subscribers(subreddit):
    """ function queries the Reddit API & returns the number of subscribers """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    # Avoid too many request errors by setting up a custom User-Agent
    headers = {'User-Agent': 'Google Chrome Version 125.0.6422.141'}

    resp = requests.get(url, headers=headers, allow_redirects=False)

    if resp.status_code == 200:
        data = resp.json().get("data").get("subscribers")
        return data
    return 0
