import string

def process_input_vigenere(input):
    input = "".join([c.lower() for c in input if c in string.ascii_letters])
    return(input)

def process_key_vigenere(key, string_length):
    expanded_key = key
    expanded_key_length = len(expanded_key)
    while expanded_key_length < string_length:
        expanded_key = expanded_key + key
        expanded_key_length = len(expanded_key)
    return(expanded_key)

def find_key_position(alphabet, letter, key_position, expanded_key):
    position = alphabet.find(letter)
    key_character = expanded_key[key_position]
    key_character_position = alphabet.find(key_character)
    key_position = key_position + 1
    return(position, key_position, key_character_position)

def vigenere_encrypt(plaintext, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted = ""
    plaintext=process_input_vigenere(plaintext)
    key= process_input_vigenere(key)
    expanded_key=process_key_vigenere(key, len(plaintext))
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

def vigenere_decrypt(ciphertext, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    decrypted = ""
    ciphertext = process_input_vigenere(ciphertext)
    key= process_input_vigenere(key)
    expanded_key=process_key_vigenere(key, len(ciphertext))
    key_position = 0
    for letter in ciphertext:
        if letter in alphabet:
            position, key_position, key_character_position = find_key_position(alphabet, letter, key_position, expanded_key)
            new_position = (position - key_character_position) % 26
            new_character = alphabet[new_position]
            decrypted = decrypted + new_character
        else:
            decrypted = decrypted + letter
    return(decrypted)