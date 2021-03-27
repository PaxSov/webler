#!/usr/bin/env python3
# Webler, a command line program that gives info about a url

import requests, sys, re

url = sys.argv[1]
isSecure = 2 # 0 = url secure | 1 = not secure | 2 = unreachable

def helpMessage():
    print('Webler, a command line program that gives info about a url')
    print('Usage: webler {url}')
    print('This program uses the MIT license | THERE IS NO WARRENTY')

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
            isSecure = 0
        except:
            try:
                requests.get("http://" + str(url))
                print("Url is insecure")
                isSecure = 1
            except:
                print("Url is unreachable | Program Aborting")
                isSecure = 0
                stop()

def writeTxt(isSecure):
    if isSecure == 0:
        open('output.txt', 'a').write('https = true')
    elif isSecure == 1:
        open('output.txt', 'a').write('https = false')
    else:
        open('output.txt', 'a').write('https = N/A')


try:
    secureCheck()
    writeTxt(isSecure)
except:
    pass


# Add help option
# Use argparse
