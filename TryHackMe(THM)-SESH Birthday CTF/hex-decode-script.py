#!/usr/bin/env python3

import binascii

hex_str = 'HEX STRINGS HERE'

# s.replace(" ", "")

unhex_str = binascii.unhexlify(hex_str.replace(" ", ""))

print(unhex_str)
