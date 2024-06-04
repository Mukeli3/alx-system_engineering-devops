#!/usr/bin/python3
"""
Contains def top_ten(subreddit) function
"""
import requests


def top_ten(subreddit):
    """ function queries the Reddit API and prints the titles of the first
     10 hot posts listed for a given subreddit
     Return: None, if not a valid subreddit """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    # Avoid too many request errors by setting up a custom User-Agent
    headers = {'User-Agent': 'Google Chrome Version 125.0.6422.141'}

    resp = requests.get(url, headers=headers, allow_redirects=False)

    if resp.status_code == 200:
        data_list = resp.json().get("data").get("children")
        for i in range(0, 10):
            print(data_list[i].get("data").get("title"))
    else:
        print(None)
