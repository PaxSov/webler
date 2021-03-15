#!/usr/bin/env python3
# Webler, a command line program that gives info about a url
# Branch: options-test


import requests, sys, re

def helpMessage():
    print('Webler, a command line program that gives into about a url')
    print('Usage: webler {option} {url}')
    print('Option 1 = google.com')
    print('Option 2 = https://google.com')
    print('Option 3 = www.https://google.com')
    print('This program uses the MIT license | THERE IS NO WARRENTY')

try:
    url = sys.argv[2]
    opt = sys.argv[1]
except:
    helpMessage()

def secureCheck(optSelect):
    if optSelect == 1:
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
        re.sub('https://','',url)
        re.sub('http://','',url)
        try:
            requests.get("https://" + str(url))
            print("Url is secure")
        except:
            try:
                requests.get("http://" + str(url))
                print("Url is insecure")
            except:
                print("Url is unreachable")
    elif optSelect == 3:
        try:
            requests.get(str(url))
            print("Url is secure")
        except:
            try:
                requests.get("http://" + str(url))
                print("Url is insecure")
            except:
                print("Url is unreachable")



try:
    secureCheck(optSelect)
except:
    pass


# TODO: Allow full url to be entered
# TODO: Option 0 = google.com entered | Option 1: https://google.com entered | Option 2: www.https://google.com entered
# The different functions are for then all to work
# Add help option
# Use argparse
# Option 0 = default
