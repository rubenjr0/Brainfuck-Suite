def clean(s):
    return s.replace('\t', '').replace('\n', '').strip()


def justify(s):
    s = list(s)
    for c in range(len(s)):
        if c > 0 and c % 66 == 0:
            s.insert(c, '\n')
    return ''.join(s)


def compress(src):
    src = clean(src)
    actual = src[0]
    c = 1
    csrc = ''
    for i in range(1, len(src)):
        if src[i] == actual:
            c += 1
        else:
            csrc += 'i{}f{}k'.format(c, actual)
            actual = src[i]
            c = 1
    return bytearray(justify(csrc).encode('utf-8'))


def decompress(csrc):
    csrc = clean(csrc)
    actual = ''
    c = ''
    dsrc = ''
    startParse = False
    fetchActual = False
    for i in range(0, len(csrc)):
        if csrc[i] == 'i':
            startParse = True
        elif csrc[i] == 'f':
            startParse = False
            c = int(c)
            fetchActual = True
        elif startParse:
            c += csrc[i]
        elif fetchActual:
            actual = csrc[i]
            fetchActual = False
        elif csrc[i] == 'k':
            dsrc += actual * int(c)
            actual = ''
            c = ''
    return dsrc


def read(fnc, m='r'):
    with open(input('Filename: ') + ('.bf' if (m == 'r') else '.bfc')) as f:
        return fnc(f.read())


def save(src, m='w+'):
    with open(input('Filename: ') + ('.bf' if (m == 'w+') else '.bfc'), m) as f:
        f.write(src)


opt = input('(c)ompress / (d)ecompress > ')
if opt is 'c':
    save(read(compress), 'wb+')
elif opt is 'd':
    save(read(decompress, 'rb'))
