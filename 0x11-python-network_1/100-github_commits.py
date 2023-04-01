#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner_name, repo_name)

    response = requests.get(url)

    for i in range(10):
        sha = response.json()[i].get('sha')
        author_name = response.json()[i].get('commit').get('author').get('name')
        print("{}: {}".format(sha, author_name))
