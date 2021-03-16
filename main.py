#!/usr/bin/env python3
# Webler, a command line program that gives info about a url

import requests, sys

url = sys.argv[1]

def helpMessage():
    print('Webler, a command line program that gives info about a url')
    print('Usage: webler {url}')
    print('This program uses the MIT license | THERE IS NO WARREATY')

try:
    url = sys.argv[1]
except:
    helpMessage()

def secureCheck():
        try:
            re.sub('https://','',url)  
            re.sub('http://','',url)   
            re.sub('www.','',url)
            requests.get(str(url))
            print("Url is secure")
        except:
            try:
                requests.get("http://" + str(url))
                print("Url is insecure")
            except:
                print("Url is unreachable")



try:
    secureCheck()
except:
    pass


# Add help option
# Use argparse
