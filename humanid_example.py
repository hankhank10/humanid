# example python code showing how to request a human readable quasi-unique ID or key from the humanid api
# full documentation at humanid.hankapi.com
# provided without warranty

import requests
import json

def get_simple_text():
    r = requests.get("http://humanid.hankapi.com/text")
    return r.text

def get_json():
    r = requests.get("http://humanid.hankapi.com/json")
    return r.text

print ()
print ("Simple text example:", get_simple_text())
print ()
print ("JSON example:", json.dumps(get_json()))
print ()