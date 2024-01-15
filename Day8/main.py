alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    if direction == "decrypt":
        shift = shift * -1

    result = ''
    for letter in range(len(text)):
        index = alphabet.index(text[letter]) + shift
        if index > len(alphabet):
            index = index % len(alphabet)
        result += alphabet[index]
    print(result)

def encrypt(text, shift):
    encrypt_text = ''
    for letter in range(len(text)):
        index = alphabet.index(text[letter]) + shift
        if index > len(alphabet):
            index = index % len(alphabet)
        encrypt_text += alphabet[index]
    
    print(encrypt_text)

def dencrypt(text, shift):
    encrypt_text = ''
    for letter in range(len(text)):
        index = alphabet.index(text[letter]) - shift
        if index * -1 > len(alphabet):
            index = index % len(alphabet) * -1
        encrypt_text += alphabet[index]
    
    print(encrypt_text)   

should_end = False
while not should_end:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  caesar(text, shift, direction)

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Goodbye")

