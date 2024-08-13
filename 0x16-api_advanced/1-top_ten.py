#!/usr/bin/python3
import requests

def top_ten(subreddit):
    """
    Queries the Reddit API to get the titles of the first 10 hot posts in a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None: Prints the titles of the top 10 hot posts or None if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 302:
            print(None)  # Redirect indicates an invalid subreddit
            return
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            for i in range(min(10, len(posts))):
                print(posts[i].get('data', {}).get('title'))
        else:
            print(None)
    except Exception:
        print(None)
