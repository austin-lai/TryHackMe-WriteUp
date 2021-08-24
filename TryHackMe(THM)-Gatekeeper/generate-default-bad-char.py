#!/usr/bin/env python3
from __future__ import print_function

# To generate default bad char - this is applicable to every single buffer overflow

listRem = ''.split('\\x')

for x in range(1, 256):
    if '{:02x}'.format(x) not in listRem:
        print('\\x' + '{:02x}'.format(x), end='')
print()
