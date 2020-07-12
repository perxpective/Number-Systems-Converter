import binascii
output = ''

print('[1] convert to binary')
print('[2] covnert to hexadecimals')
print('[3] convert to octodecimals')
print('[4] decode to hexadecimal to text')
option = input('select option: ')
while not (option == '1' or option == '2' or option == '3' or option == '4'):
    print('invalid input')
    option = input('select option: ')

# text to ascii to binary
if option == '1':
    string = input('enter string to cipher: ')
    for char in string:
      char_num = bin(ord(char))
      output += char_num[2:]

# text to ascii to hexadecimals
elif option == '2':
    string = input('enter string to cipher: ')
    for char in string:
      char_num = hex(ord(char))
      output += char_num[2:]


# text to ascii to octodecimals
elif option == '3':
    string = input('enter string to cipher: ')
    for char in range(len(string)):
        char_num = oct(ord(string[char]))
        output += char_num[2:]

# deciphering
elif option == '4':
  string = input('enter string to decipher: ')
  output = binascii.unhexlify(string).decode()

print('value: ', output)
