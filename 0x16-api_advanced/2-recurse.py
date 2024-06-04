#!/usr/bin/python3
"""
Contains def recurse(subreddit, hot_list=[]) function
"""
import requests


def recurse(subreddit, hot_list=[], params=None):
    """ recursive function, queries the Reddit API and returns a list
    containing titles of all hot articles for a subreddit
    Returns:
        None, if no results found
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    # Avoid too many request errors by setting up a custom User-Agent
    headers = {'User-Agent': 'Google Chrome Version 125.0.6422.141'}

    resp = requests.get(url,
                        headers=headers,
                        params=params,
                        allow_redirects=False)

    if resp.status_code == 200:
        data = resp.json().get("data")
        d_list = data.get("children")
        for hot in d_list:
            hot_list.append(hot.get("data").get("title"))

        later = data.get("after")

        if later:
            params = {"after": later, "limit": 100}
            recurse(subreddit, hot_list=hot_list, params=params)
            return hot_list
        return None
