def translate(text):
    length = len(text)
    src = '+' * 10 + '[>\n'
    for i in range(length):
        src += '\t' + '+' * (ord(text[i]) // 10) + '>\n'
    src += '<' * (length + 1) + '-]>\n'
    for i in range(length):
        src += '+' * (ord(text[i]) % 10) + '.>\n'
    return src


def save(fn, data):
    with open('{}.bf'.format(fn), 'w+') as f:
        f.write(data)


fn = input('Filename: ')
src = translate(input('Translate: '))
save(fn, src)

print('Saved brainfuck source code to {}.bf\nSrc:\n\n{}'.format(fn, src))
