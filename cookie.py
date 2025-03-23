import os 
import json
import requests 
import time 


print("checking if requirements are installed ")
time.sleep(2)
print()

os.system("pip install browser_cookie3")

import browser_cookie3
from email.mime.multipart import MIMEMultipart
print()
print("checked")
print() 
domain = "tradingview.com"

def getCookiesFromDomain(domain,cookieName=''):

    Cookies={}
    chromeCookies = list(browser_cookie3.chrome())

    for cookie in chromeCookies:

        if (domain in cookie.domain):
            #print (cookie.name, cookie.domain,cookie.value)
            Cookies[cookie.name]=cookie.value

    if(cookieName!=''):
        try:
            return Cookies[cookieName] #return specified cookie
        except:
            return {} #if exception raised return an empty dictionary
    else:
        return Cookies #return all cookies or nothing

getCookiesFromDomain('google.com')


