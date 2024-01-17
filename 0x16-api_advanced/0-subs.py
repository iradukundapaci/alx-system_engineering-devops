#!/usr/bin/python3
"""
 function that return number of
    subscribers for a sub reddit
"""
import requests as re


def number_of_subscribers(subreddit):
    """
        function to get subscribers for a subreddit
        subreddit: the provided sub reddit
    """

    user_agent = {'User-agent': 'Google Chrome Version 120.0.0.0'}

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    res = re.get(url, headers=user_agent)

    if (res.ok):
        content = res.json()
        try:
            return content.get("data").get("subscribers")
        except (Exception):
            return 0

    else:
        return 0
