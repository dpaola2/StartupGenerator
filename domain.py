#! /usr/bin/env python

import requests

URL = "https://testapi.internet.bs/domain/Check?Domain=%s&ApiKey=testapi&Password=testpass"

def split_equals(x):
    s = x.split("=")
    return { s[0] : s[1] }
    

def domain(dom):
    return requests.get(URL % dom).text

if __name__ == '__main__':
    main()
