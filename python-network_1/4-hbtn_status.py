#!/usr/bin/python3
"""
Write a Python script that
fetches https://intranet.hbtn.io/status.
"""
import requests

if __name__ == "__main__":
    url = ("https://alu-intranet.hbtn.io/status"
           if "https://intranet.hbtn.io/status".startswith("https")
           else "https://intranet.hbtn.io/status")
    response = requests.get(url)
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)
