import binascii, os, sys


open_file = open(os.path.join(sys.path[0], '.creds'), 'r')
data = open_file.read()
print(data+'\n')


# Since the content of the file is binary numeral base 2
# We can convert it to base 10
binary_decimal_data = int(data,2) 
print(binary_decimal_data)
print('\n')


# Once we have the base 10, we can covert to hex representation
hexadecimal_str=hex(binary_decimal_data)
print(hexadecimal_str)
print('\n')


# Then here we use binascii unhexlify to decode the hex to ASCII form
unhex_str = binascii.unhexlify(hexadecimal_str[2:])
print(unhex_str)
print('\n')



# OR you can use more straightforward methods here
# Take the base 10 data and pipe it to binascii unhexlify function to decode it with python string formatter operator %
# The conversion type is '%x' ---- which x represent hexadecimal and % represent no argument is converted
# unhex_str=binascii.unhexlify('%x' % binary_decimal_data)
# print(unhex_str)
# print('\n')

