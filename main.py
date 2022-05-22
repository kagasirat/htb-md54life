#!/usr/bin/python3

import hashlib
import requests
import sys

if len(sys.argv) != 3:
    print("Usage: python main.pyp IP PORT")
    exit(1)

# Arguments
IP = sys.argv[1]
PORT = sys.argv[2]

# Session
req = requests.session()
url = "http://" + IP + ":" + PORT
print("Target: " + url)

# Read the target website
resp = req.get(url).content
resp = resp.split(b'<h3 align=\'center\'>')[1].split(b'</h3>')[0]
print("Text: " + str(resp))

# Encrypt with md5
h = hashlib.md5(resp).hexdigest()
print("Hash: " + str(h))

# Post the answer
data = dict(hash=h)
resp = req.post(url, data)
print(resp.text)