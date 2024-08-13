#!/usr/bin/python3
import requests

def recurse(subreddit, hot_list=[]):
    """ Recursively queries the Reddit API and returns a list of hot article titles for a given subreddit. """
    
    # Define the base URL for the Reddit API
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    
    # Set the headers to use User-Agent
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    # Make the request to the Reddit API
    response = requests.get(url, headers=headers, params={'limit': 100}, allow_redirects=False)
    
    # Check if the response was successful
    if response.status_code != 200:
        return None

    # Load the response JSON data
    data = response.json()
    
    # Check if 'data' and 'children' keys are in the JSON data
    if 'data' not in data or 'children' not in data['data']:
        return None
    
    # Extract the list of articles
    articles = data['data']['children']
    
    # Add the titles of the articles to the hot_list
    hot_list.extend([article['data']['title'] for article in articles])
    
    # Check if there's more data to fetch
    after = data['data'].get('after')
    if after:
        # Recursively call the function with the next page
        next_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
        response = requests.get(next_url, headers=headers, params={'after': after, 'limit': 100}, allow_redirects=False)
        if response.status_code == 200:
            return recurse(subreddit, hot_list)
    
    return hot_list
