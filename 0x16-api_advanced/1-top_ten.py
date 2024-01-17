#!/usr/bin/python3

"""
    Prints top 10 titles for given subreddit
"""

import requests as re


def top_ten(subreddit):
    """
        function to handle the printing
        of top 10 title for a given subreddit
    """

    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    user_agent = {'User-agent': 'Google Chrome Version 120.0.0.0'}
    params = {'limit': 10}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)

    response = re.get(url, headers=user_agent, params=params)
    results = response.json()

    try:
        result_data = results.get('data').get('children')

        for i in result_data:
            print(i.get('data').get('title'))

    except Exception:
        print("None")