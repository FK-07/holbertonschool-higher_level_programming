#!/usr/bin/python3
"""Fetches a URL and handles HTTPError exceptions"""
import sys
import urllib.request
import urllib.error


if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    
    try:
        with urllib.request.urlopen(req) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
