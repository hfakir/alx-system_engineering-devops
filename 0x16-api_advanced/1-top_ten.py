#!/usr/bin/python3
"""Query Reddit API to determine subreddit sub count"""
import requests


def top_ten(subreddit):
    """Get top 10 subscribers"""
    req = requests.get(
        f"https://www.reddit.com/r/{subreddit}/hot.json",
        headers={},
        params={"limit": 10},
    )

    if req.status_code == 200:
        data = req.json().get("data")
        if data and "children" in data:
            for child in data["children"]:
                if "data" in child and "title" in child["data"]:
                    print(child["data"]["title"])
                else:
                    print("Invalid post format: ", child)
        else:
            print("No data returned from Reddit.")
    else:
        print(None)