#!/usr/bin/env python3
# Webler, a command line program that gives info about a url
# Branch: options-test


import requests, sys, re

url = sys.argv[2]
opt = sys.argv[1]

def secureCheck(optSelect):
    if optSelect == 0:
        try:
            requests.get("https://" + str(url))
            print("Url is secure")
        except:
            try:
                requests.get("http://" + str(url))
                print("Url is insecure")
            except:
                print("Url is unreachable")
    elif optSelect == 1:
        try:
            requests.get("https://" + str(url))
            print("Url is secure")
        except:
            try:
                requests.get("http://" + str(url))
                print("Url is insecure")
            except:
                print("Url is unreachable")
    elif optSelect == 2:
        try:
            requests.get(str(url))
            print("Url is secure")
        except:
            try:
                requests.get("http://" + str(url))
                print("Url is insecure")
            except:
                print("Url is unreachable")



secureCheck(optSelect)


# TODO: Allow full url to be entered
# TODO: Option 0 = google.com entered | Option 1: https://google.com entered | Option 2: www.https://google.com entered
# The different functions are for then all to work
# Add help option
# Use argparse
