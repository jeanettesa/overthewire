# Level 8-> Level 9 ("input secret")
# http://natas8.natas.labs.overthewire.org/
# Get base64 string from hex "3d3d516343746d4d6d6c315669563362", reverse string, and decode to utf-8
import base64
base64.b64decode(bytearray.fromhex("3d3d516343746d4d6d6c315669563362").decode()[::-1]).decode()

