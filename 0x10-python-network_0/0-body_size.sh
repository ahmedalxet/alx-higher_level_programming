#!/bin/bash
# This script takes a URL, sends a request to that URL using curl
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
