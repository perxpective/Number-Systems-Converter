# Number-Systems-Converter
Convert your string text into hexadecimals, octodecimals or binary.

### Initialising Variables and Modules
To start, I import the modules. If the program is run on repl.it, the `replit` module will allow the terminal to be clear when moving from one "menu" to another. Note that the replit module will not work when run externally on other IDE platforms. I will also initiate the `output` variable which will determine our converted output after various user inputs.

```
import replit
import binascii
output = ''
```

### Options
After initialising my variables and modules, I can now display a menu. The user can choose to input an option to convert text to either hexadecimals, binary or octodecimals.

```
print('[1] convert to binary')
print('[2] covnert to hexadecimals')
print('[3] convert to octodecimals')
print('[4] decode to text')
option = input('select option: ')
```

I run a `while` loop to validate the user input of the options above to prompt the user to select an option above based on the options above.


```
while not (option == '1' or option == '2' or option == '3' or option == '4'):
    print('invalid input')
    option = input('select option: ')
```

## Respective Encryptions
Now I each code according to the user input of the four options above in order to encrypt the string inputs into the respective number systems.

### Encrypting Strings to Binary
```
if option == '1':
    string = input('enter string to cipher: ')
    for char in range(len(string)):
        char_num = bin(ord(string[char]))
        output += char_num[2:]
```

If user input is 1, which is to convert the string into binary, a `for` loop is used to respectively convert each character in the string into a ASCII value (this is done using the `ord()` function. Simultaneously, the ASCII value is converted into binary values and then stitched together to form a series of binary values in the variable `output`.

> Note: Whenever an integer (In this case, the ASCII value of a character) is converted into binary, Python tends to add `0b` into the binary value to show that it is indeed a binary value, and not a series of integers. Thus, it is important to slice the first two characters (`0b`) of that one character's binary value, so that there aren't any `0b`s mixing around in the `output` variable.

### Encrypting Strings to Hexadecimals
```
elif option == '2':
    string = input('enter string to cipher: ')
    for char in range(len(string)):
        char_num = hex(ord(string[char]))
        output += char_num[2:]
```

If the user input is 2, the string will be encoded into hexadecimals. This is the exact same algorithm as the code we seen in ciphering strings into binary. The only different is that in the `for` loop, `char_num` stores the hexadecimal of the ASCII value  using the `hex()` function.

### Encrypting Strings to Octodecimals
```
elif option == '3':
    string = input('enter string to cipher: ')
    for char in range(len(string)):
        char_num = oct(ord(string[char]))
        output += char_num[2:]
```

If user input is 3, the string will be encoded into octdecimals. Again, replace the first function with the `oct()` function to convert the character's ASCII value into octodecimals into `char_num`

## Decrypting Number Systems to Text
```
elif option == '4':
    print('- put 0x if hexadecimal')
    print('- put 0b if binary')
    print('- put 0o if octodecimal')
    string = input('enter string to decipher: ')
    while not ('0x' in string or '0b' in string or '0o' in string):
        print('oops! something went wrong.')
        string = input('enter string to decipher[minimum 8 chars]: ')
```
Users can decode their encrypted messages by selecting the option 4. In order to determine the values of the number systems, number value prefixes must be inputted. This is because if prefixes are not added, this will give an invalid syntax. We want to convert the raw encoded value (bin, hex, oct) integers into denary values. This will also not work if the series of values are in string. Otherwise, the prompt will be iterated in a `while` loop until the user can give a required input.

> Note: `0b`: binary;
`0x`: hexadecimal;
`0o`: octodecimal;

### Decoding Encrypted Values
```
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
        output = bytearray.fromhex(string).decode()

    elif '0o' in string:
        output.replace("0o","")
        output += chr(int(string[0:4],8))
        for char in range(1,len(string)//3+1):
            output += chr(int(string[char*3+1:char*3+4], 8))

print('value: ', output)
```

Using the `bytearray.fromhex(string).decode()` function, we can decode hexadecimals into strings.

Other values can be decoded using the `for` loop.
