#!/usr/bin/env python3
# Webler, a command line program that gives info about a url

import requests, argparse, re, os
from selenium import webdriver
from time import sleep
from socket import gethostbyname
from ipwhois import IPWhois
from pprint import pprint
# from iplookup import lookup

# Argparse Things
parser = argparse.ArgumentParser()
parser.add_argument("url", type=str, help="Enter a Url e.g python.org")
parser.add_argument("-e", "--export-to-txt", dest="makeTxt", help="Export The Program's Output To a Text File", action="store_true")
parser.add_argument("-s", "--save-screenshot", dest="saveScreenShot", help="Save a screenshot of the url", action="store_true")
parser.add_argument("-i", "--show-ip", dest="showIp", help="Show ip of url", action="store_true")
parser.add_argument("-ip", "--show-ip-info", dest="showIpInfo", help="Show information about the ip of the url", action="store_true")
args = parser.parse_args()

# Alias
getDomainIp = gethostbyname("www." + args.url)
# ipLookUp = IPWhois(getDomainIp)
ipInfo = getDomainIp.IPWhois.lookup()

if args.makeTxt:
    txt = True
    file = open('output.txt', 'a+')
    file.write("Url is ", args.url)
    file.close

def getScreenShot(browser):
    if browser == 1:
        driver = webdriver.Chrome()
    elif browser == 2:
        driver = webdriver.Firefox()

    driver.get(str("http://" + args.url))
    sleep(1)

    driver.get_screenshot_as_file("screenshot.png")

    driver.quit()
    
    cwd = os.getcwd()
    if txt == True:
        file.write("A Screenshot was taken")
        file.close()
    else:
        pass
    if browser == 2:
        geckoLogFile = os.path.join(cwd, "geckodriver.log")
        os.remove(geckoLogFile)
    else:
        pass


if args.url:
    pass
else:
    print("You need to enter a url")
    exit()

def secureCheck():
    args.url = str(args.url)
    args.url = re.sub(r"www", "", args.url)    
    args.url = re.sub(r"https://", "", args.url)
    args.url = re.sub(r"http://", "", args.url)
    try:
        requests.get("https://" + str(args.url))
        print("Url is secure")
        if txt == True:
            file.write("Url Is Secure")

    except:
        try:
            requests.get("http://" + str(args.url))
            print("Url is insecure")
        except:
            print("Url is unreachable")

def ipOption():
    print("Url Ip: ", getDomainIp)
    pprint(ipInfo)
    if txt == True:
        file.write(pprint(ipInfo))
        file.close()

try:
    secureCheck()
except:
    pass
if args.saveScreenShot:
    try:
        getScreenShot(1)
    except:
        print("Do you have google chrome installed? | Attemping Firefox / Geckodriver")
        getScreenShot(2)
try:
    secureCheck()
except:
    pass
# TODO finish that export to txt feature
