# Number-Systems-Converter
Convert your string text into hexadecimals, octodecimals or binary.

### Initialising Variables and Modules
To start, I import the modules. I will also initiate the `output` variable which will determine our converted output after various user inputs.

``` python
import binascii
output = ''
```

### Options
After initialising my variables and modules, I can now display a menu. The user can choose to input an option to convert text to either hexadecimals, binary or octodecimals.

``` python
print('[1] convert to binary')
print('[2] covnert to hexadecimals')
print('[3] convert to octodecimals')
print('[4] decode to hexadecimals to text')
option = input('select option: ')
```

I run a `while` loop to validate the user input of the options above to prompt the user to select an option above based on the options above.


``` python
while not (option == '1' or option == '2' or option == '3' or option == '4'):
    print('invalid input')
    option = input('select option: ')
```

## Respective Encryptions
Now I each code according to the user input of the four options above in order to encrypt the string inputs into the respective number systems.

### Encrypting Strings to Binary
``` python
if option == '1':
    string = input('enter string to cipher: ')
    for char in range(len(string)):
        char_num = bin(ord(string[char]))
        output += char_num[2:]
```

If user input is 1, which is to convert the string into binary, a `for` loop is used to respectively convert each character in the string into a ASCII value (this is done using the `ord()` function. Simultaneously, the ASCII value is converted into binary values and then stitched together to form a series of binary values in the variable `output`.

> Note: Whenever an integer (In this case, the ASCII value of a character) is converted into binary, Python tends to add `0b` into the binary value to show that it is indeed a binary value, and not a series of integers. Thus, it is important to slice the first two characters (`0b`) of that one character's binary value, so that there aren't any `0b`s mixing around in the `output` variable.

### Encrypting Strings to Hexadecimals
``` python
elif option == '2':
    string = input('enter string to cipher: ')
    for char in range(len(string)):
        char_num = hex(ord(string[char]))
        output += char_num[2:]
```

If the user input is 2, the string will be encoded into hexadecimals. This is the exact same algorithm as the code we seen in ciphering strings into binary. The only different is that in the `for` loop, `char_num` stores the hexadecimal of the ASCII value  using the `hex()` function.

### Encrypting Strings to Octodecimals
``` python
elif option == '3':
    string = input('enter string to cipher: ')
    for char in range(len(string)):
        char_num = oct(ord(string[char]))
        output += char_num[2:]
```

If user input is 3, the string will be encoded into octdecimals. Again, replace the first function with the `oct()` function to convert the character's ASCII value into octodecimals into `char_num`

## Decrypting Number Systems to Text

Users can decode their encrypted messages by selecting the option 4. In order to determine the values of the number systems, number value prefixes must be inputted. This is because if prefixes are not added, this will give an invalid syntax. We want to convert the raw encoded hexadecimal values into denary values. This will also not work if the series of values are in string. Otherwise, the prompt will be iterated in a `while` loop until the user can give a required input.

### Decoding Encrypted Values
``` python
    
    elif option == '4':
      string = input('enter string to decipher: ')
      output = binascii.unhexlify(string).decode()

print('value: ', output)
```

Using the `bytearray.fromhex(string).decode()` function, we can decode hexadecimals into strings.

Other values can be decoded using the `for` loop.

## Dry Run

### Option Menu
```
[1] convert to binary
[2] covnert to hexadecimals
[3] convert to octodecimals
[4] decode to text
select option: 5
invalid input
select option: 
```
### Encrypting to Binary
```
select option: 1
enter string to cipher: hello world
value:  1101000110010111011001101100110111110000011101111101111111001011011001100100
```

### Encrypting to Hexadecimals
```
select option: 2
enter string to cipher: hello world
value:  68656c6c6f20776f726c64
```

### Encrypting to Octodecimals
```
select option: 3
enter string to cipher: hello world
value:  15014515415415740167157162154144
```

### Decrypting
```
# hexadecimal-example
select option: 4
- put 0x if hexadecimal
- put 0b if binary
- put 0o if octodecimal
enter string to decipher: 0x68656c6c6f20776f726c64
value:  hello world
```

