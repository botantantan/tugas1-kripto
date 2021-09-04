import string
import itertools

def process_input_vigenere(input):
    input = "".join([c.lower() for c in input if c in string.ascii_letters])
    return(input)

def process_key_vigenere(key, plaintext):
    expanded_key = key
    string_length = len(plaintext)
    expanded_key_length = len(expanded_key)

    while expanded_key_length < string_length:
        expanded_key = expanded_key + plaintext
        expanded_key_length = len(expanded_key)

    expanded_key = expanded_key[0:string_length]
    return(expanded_key)

def find_key_position(alphabet, letter, key_position, expanded_key):
    position = alphabet.find(letter)
    key_character = expanded_key[key_position]
    key_character_position = alphabet.find(key_character)
    key_position = key_position + 1
    return(position, key_position, key_character_position)

def vigenere_autokey_encrypt(plaintext, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted = ""

    plaintext=process_input_vigenere(plaintext)

    key= process_input_vigenere(key)
    expanded_key=process_key_vigenere(key, plaintext)
    key_position = 0

    for letter in plaintext:
        if letter in alphabet:
            position, key_position, key_character_position=find_key_position(alphabet, letter, key_position, expanded_key)
            new_position = (position + key_character_position)% 26
            new_character = alphabet[new_position]
            encrypted = encrypted + new_character
        else:
            encrypted = encrypted + letter

    return(encrypted)

def vigenere_autokey_decrypt(ciphertext, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    decrypted = ""

    ciphertext = process_input_vigenere(ciphertext)

    string_length = len(ciphertext)

    key= process_input_vigenere(key)

    key_position = 0

    for letter in ciphertext:
        if letter in alphabet:
            position, key_position, key_character_position = find_key_position(alphabet, letter, key_position, key)
            new_position = (position - key_character_position) % 26
            new_character = alphabet[new_position]
            decrypted = decrypted + new_character
            if len(key)<len(ciphertext):
                key += new_character
        else:
            decrypted = decrypted + letter
    return(decrypted)

def print5char(str):
	start = 0
	while start+5 < len(str):
		print(str[start:start+5],end=" ")
		start+=5
	print(str[start:len(str)])

# Testing
print5char(vigenere_autokey_encrypt("aku suka kucing yang imut kaya angora anjing kontol", "hello man"))
print(vigenere_autokey_decrypt("hofdi waxum cfaia xakuh zialg izahb aynjv tubon gxt", "hello man"))