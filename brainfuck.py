def run(src):
    src = src.strip()
    # print('Running source:\n{}\n'.format(src))
    ptr = 0
    mem = [0] * 8
    jump = False
    lsp = 0
    PC = 0
    while PC < len(src):
        if src[PC] in '><+-[].,' and not jump:
            if src[PC] is '>':
                ptr += 1
                if len(mem) <= ptr:
                    mem += [0] * 8
            elif src[PC] is '<':
                ptr -= 1
            elif src[PC] is '+':
                mem[ptr] += 1
            elif src[PC] is '-':
                mem[ptr] -= 1
            elif src[PC] is '[':
                lsp = PC
                if mem[ptr] is 0:
                    jump = True
            elif src[PC] is ']':
                if mem[ptr] is not 0:
                    PC = lsp
            elif src[PC] is '.':
                print(chr(mem[ptr]), end='')
            elif src[PC] is ',':
                mem[ptr] = input().encode()
        if jump and src[PC] is ']':
            jump = False
        PC += 1


def read(fn):
    with open(fn) as f:
        src = f.read()
        src = src.replace(' ', '')
        src = src.replace('\n', '')
        return src


# run(input('src /> '))
try:
    run(read('{}.bf'.format(input('Filename: '))))
except:
    print('error')
