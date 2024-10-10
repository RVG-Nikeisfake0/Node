# b64.py (necessary file)
import re, struct, binascii

__all__ = [
    'b64encode', 'b64decode', 'b32encode', 'b32decode', 'b32hexencode', 'b32hexdecode',
    'b16encode', 'b16decode', 'b85encode', 'b85decode'
]

def b64encode(s, altchars=None):
    encoded = binascii.b2a_base64(s, newline=False)
    if altchars is not None:
        return encoded.translate(bytes.maketrans(b'+/', altchars))
    return encoded

def b64decode(s, altchars=None, validate=False):
    s = s.encode('ascii') if isinstance(s, str) else s
    if altchars is not None:
        s = s.translate(bytes.maketrans(altchars, b'+/'))
    return binascii.a2b_base64(s, strict_mode=validate)

def b32encode(s):
    return binascii.b32encode(s)

def b32decode(s):
    return binascii.b32decode(s)

def b32hexencode(s):
    return binascii.b32hexencode(s)

def b32hexdecode(s):
    return binascii.b32hexdecode(s)

def b16encode(s):
    return binascii.b16encode(s)

def b16decode(s):
    return binascii.b16decode(s)

def b85encode(s):
    return binascii.b85encode(s)

def b85decode(s):
    return binascii.b85decode(s)
    