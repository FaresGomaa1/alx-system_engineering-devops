#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API to get the number of subscribers of a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers of the subreddit, or 0 if the subreddit is invalid.
    """
    # Define the API URL
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    
    # Set a custom User-Agent to avoid 'Too Many Requests' errors
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        # Make the GET request to Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check for a redirect response (status code 3xx)
        if response.status_code == 302:
            return 0
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()
            return data.get('data', {}).get('subscribers', 0)
        else:
            return 0
    except Exception:
        return 0
