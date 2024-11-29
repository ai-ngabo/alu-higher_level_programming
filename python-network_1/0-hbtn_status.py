#!/usr/bin/python3
"""A script that fetches https://alu-intranet.hbtn.io/status
with the  use of  urllib."""
from urllib import request

if __name__ == "__main__":
    with request.urlopen(
            "https://alu-intranet.hbtn.io/status"
            if "https://intranet.hbtn.io/status".startswith("https")
            else "https://intranet.hbtn.io/status") as response:
        html = response.read()
        print("Body response:")
        print("\t- type:", type(html))
        print("\t- content:", html)
        print("\t- utf8 content:", html.decode("utf-8"))
