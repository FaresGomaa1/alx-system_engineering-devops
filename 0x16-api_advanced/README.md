# 0x16 - API Advanced

This project focuses on advanced API interactions, particularly using Python to work with the Reddit API. It includes several tasks that involve querying APIs, handling JSON data, pagination, and recursion.

## Project Structure

- `0-subs.py`: Contains the function to query the Reddit API and return the number of subscribers for a given subreddit.
- `0-main.py`: A script to test the `number_of_subscribers` function by taking a subreddit name as a command-line argument.

## Tasks

### 0. How Many Subs?

**Objective**: Write a function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0.

**Requirements**:
- **Prototype**: `def number_of_subscribers(subreddit)`
- If not a valid subreddit, return 0.
- Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.

**Implementation**:
- The `number_of_subscribers` function is defined in `0-subs.py`.
- It uses the `requests` module to make an HTTP GET request to the Reddit API.
- Handles redirects and invalid subreddits by checking for HTTP status code 302.
- Returns the number of subscribers if the request is successful, otherwise returns 0.

**Example Usage**:
To run the main script and check the number of subscribers for a subreddit, use:
```bash
python3 0-main.py programming
