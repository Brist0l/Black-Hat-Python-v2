# chr: int to unicode str
# repr: outputs the `offical` form,eg: repr('\n') -> '\n' instead of a newline
# this filters out stuff like '\x01' and instead of that pushes a '.'
HEX_FILTER = ''.join(
    [((len(repr(chr(i))) == 3) and chr(i)) or '.' for i in range(256)])

def hexdump(src,length = 16,show=True):
    if isinstance(src,bytes):
        src = src.decode()
    
    results = []
    for i in range(0,len(src),length):
        word = str(src[i:i+length])

        # will convert all the non-ascii chars to `.`
        printable = word.translate(HEX_FILTER) 
        hexa = ' '.join([f'{ord(c):02x}' for c in word])
        hexwidth = length*3

        results.append(f'{i:04x}  {hexa:<{hexwidth}}{printable}')
        if show:
            for line in results:
                print(line)
            else:
                return results
                


