#!/usr/bin/python3
import requests
import re
from collections import Counter

def count_words(subreddit, word_list):
    """ Recursively queries the Reddit API, parses titles, and counts occurrences of keywords. """
    
    def fetch_hot_articles(subreddit, after=None):
        """ Fetches hot articles from Reddit API. """
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
        headers = {'User-Agent': 'Mozilla/5.0'}
        params = {'limit': 100}
        if after:
            params['after'] = after
        
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code != 200:
            return None
        
        data = response.json()
        if 'data' not in data or 'children' not in data['data']:
            return None
        
        return data
    
    def process_articles(data, counter):
        """ Processes the articles and updates the keyword counter. """
        articles = data['data']['children']
        titles = [article['data']['title'].lower() for article in articles]
        
        for title in titles:
            for word in word_list:
                word_lower = word.lower()
                # Use regex to match the whole word and ignore case
                occurrences = len(re.findall(r'\b{}\b'.format(re.escape(word_lower)), title, re.IGNORECASE))
                counter[word_lower] += occurrences
    
    def recurse(subreddit, counter, after=None):
        """ Recursively fetches articles and processes them. """
        data = fetch_hot_articles(subreddit, after)
        if not data:
            return
        
        process_articles(data, counter)
        
        after = data['data'].get('after')
        if after:
            recurse(subreddit, counter, after)
    
    # Initialize the counter and start recursion
    counter = Counter()
    recurse(subreddit, counter)
    
    # Sort the results first by count (descending), then alphabetically (ascending)
    sorted_keywords = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
    
    for word, count in sorted_keywords:
        print(f"{word}: {count}")
