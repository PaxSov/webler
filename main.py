#!/usr/bin/env python3
# Webler, a command line program that gives info about a url

import requests, sys, signal

url = sys.argv[1]

try:
    reqUrl = requests.get("https://" + str(url))
    print("Url is secure")
except:
    print("Url is insecure")

# TODO: Make function time out after 10s and print("Url is unreachable, possibly insecure"), a scenario happens like this with go.com
# Allow full url to be entered
