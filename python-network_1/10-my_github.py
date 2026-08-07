#!/usr/bin/python3
"""Uses the GitHub API to display user id with Basic Authentication"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"

    r = requests.get(url, auth=(username, password))
    print(r.json().get('id'))
