#!/usr/bin/python3
"""
fetches https://api.github.com/user and displays id
"""
from sys import argv

from requests import get

if __name__ == "__main__":
    url = "https://api.github.com/user"
    response = get(url, auth=(argv[1], argv[2]))
    print(response.json().get("id"))
