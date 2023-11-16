#!/bin/bash
# This script takes in a URL, sends a GET request to the URL using curl, and displays the body of the response (only for 200 status code)
curl -s -X GET "$1" -w "%{http_code}" -o /dev/null | [ "$(curl -s -X GET "$1")" = "200" ] && curl -s -X GET "$1" || echo ""
