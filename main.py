#!/usr/bin/env python3
# Webler, a command line program that gives info about a url

import requests, sys

url = sys.argv[1]

def secureCheck():
    try:
        requests.get("https://" + str(url))
        print("Url is secure")
    except:
        try:
            requests.get("http://" + str(url))
            print("Url is insecure")
        except:
            print("Url is unreachable")

secureCheck()


# TODO: Allow full url to be entered
