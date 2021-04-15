#!/usr/bin/env python3
# Webler, a command line program that gives info about a url

import requests, re, argparse

# Argparse Things
parser = argparse.ArgumentParser()
parser.add_argument("url", help="Enter a Url e.g python.org")
parser.add_argument("-e", "--export-to-txt", help="Export The Program's Output To a Text File", action="store_true")
parser.add_argument("-w", "--web-of-trust", help="Show web of trust score", action="store_true")
parser.add_argument("-i", "--show-ip", help="Show ip of url", action="store_true")
parser.add_argument("-ip", "--show-ip-info", help="Show information about the ip of the url", action="store_true")
args = parser.parse_args()

if args.url:
    pass
else:
    print("You need to enter a url")
    exit()

def secureCheck():
    re.sub('www', '', args.url)    
    re.sub('https://','',args.url)
    re.sub('http://','',args.url)
    try:
        requests.get("https://" + str(args.url))
        print("Url is secure")
    except:
        try:
            requests.get("http://" + str(args.url))
            print("Url is insecure")
        except:
            print("Url is unreachable")



try:
    secureCheck()
except:
    pass
