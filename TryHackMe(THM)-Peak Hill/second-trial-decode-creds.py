import binascii, os, sys, pickle


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



# Use the load method to unpickle the data into a python object
unpickled_data = pickle.loads(unhex_str)
print(unpickled_data)
print('\n')


# Set username and password variables to store the username and password, as well as turn it into dictionaries
username = ''
password = ''
unpickled_data = dict(unpickled_data)


# Use for loop to iterates 27 times as the highest number is 27 for the password, which you can check on the data 'ssh_pass27'
for i in range(28):
  
  # Since the amount of characters in the username is 6, we will need to set up error handling to error message given.
  try:
    username += unpickled_data[f'ssh_user{i}']
  except:
    pass
  password += unpickled_data[f'ssh_pass{i}']
  
print(f'username = {username}')
print(f'password = {password}')

