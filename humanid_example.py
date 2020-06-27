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