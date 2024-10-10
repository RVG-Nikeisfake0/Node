def BCSE(x: str, y: str, m: str='e' or 'd'):
    return ''.join(chr((ord(a) + (ord(b) if m == 'e' else -ord(b))) % 256) for a, b in zip(x, (y * (len(x) // len(y) + 1))[:len(x)])).encode('utf-8')
    