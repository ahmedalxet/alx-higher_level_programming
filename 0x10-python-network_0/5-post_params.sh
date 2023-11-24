#!/bin/bash
# This script takes in a URL as an argument, sends a POST request to the URL with variables email and subject, and displays the body of the response
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
