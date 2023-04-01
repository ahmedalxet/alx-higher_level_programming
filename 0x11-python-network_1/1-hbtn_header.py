#!/usr/bin/python3
import urllib.request
import sys

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    header = response.info()
    x_request_id = header.get('X-Request-Id')

print(x_request_id)
