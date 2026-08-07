#!/usr/bin/python3
"""Sends a POST request with a letter parameter and parses JSON response"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    url = "http://0.0.0.0:5000/search_user"
    payload = {'q': q}

    try:
        r = requests.post(url, data=payload)
        json_obj = r.json()
        if json_obj:
            print("[{}] {}".format(json_obj.get('id'), json_obj.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
