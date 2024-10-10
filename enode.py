def enode(x: str, y: str):
    return ''.join(chr(ord(a) ^ ord(y[i % len(y)])) for i, a in enumerate(x)).encode('utf-8')
    