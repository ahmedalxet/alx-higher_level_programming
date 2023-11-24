#!/bin/bash
# This script takes in a URL, sends a GET request to the 
# URL using curl, and displays the body of the response 
# for a status code of 200
curl -s -X GET -i "$1" | grep -i "HTTP/1.1 200 OK" -A 1000 | sed -n '/^$/,$p'
