import replit
import binascii
output = ''

print('[1] convert to binary')
print('[2] covnert to hexadecimals')
print('[3] convert to octodecimals')
print('[4] decode to text')
option = input('select option: ')
while not (option == '1' or option == '2' or option == '3' or option == '4'):
    print('invalid input')
    option = input('select option: ')

# text to ascii to binary
if option == '1':
    string = input('enter string to cipher: ')
    for char in range(len(string)):
        char_num = bin(ord(string[char]))
        output += char_num[2:]

# text to ascii to hexadecimals
elif option == '2':
    string = input('enter string to cipher: ')
    for char in range(len(string)):
        char_num = hex(ord(string[char]))
        output += char_num[2:]

# text to ascii to octodecimals
elif option == '3':
    string = input('enter string to cipher: ')
    for char in range(len(string)):
        char_num = oct(ord(string[char]))
        output += char_num[2:]

# deciphering
elif option == '4':
    print('- put 0x if hexadecimal')
    print('- put 0b if binary')
    print('- put 0o if octodecimal')
    string = input('enter string to decipher: ')
    while not ('0x' in string or '0b' in string or '0o' in string):
        print('oops! something went wrong.')
        string = input('enter string to decipher[minimum 8 chars]: ')

    if '0b' in string:
        string = string.replace("0b", "")
        bin_values = string.split()
        output = ""
        for bin_value in bin_values:
            integer = int(bin_value, 2)
            char = chr(integer)
            output += char
            


    elif '0x' in string:
        string = int(string, 2)
        output = bytearray.fromhex(string).decode('utf-8')

    elif '0o' in string:
        output.replace("0o","")
        output += chr(int(string[0:4],8))
        for char in range(1,len(string)//3+1):
            output += chr(int(string[char*3+1:char*3+4], 8))

print('value: ', output)
