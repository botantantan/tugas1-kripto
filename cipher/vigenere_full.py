import string
import random
import re

alphabet_uppercase = list(string.ascii_uppercase)
regex = re.compile('[^a-zA-Z]')

def process_input_vigenere(input):
    input = "".join([c.upper() for c in input if c in string.ascii_letters])
    return(input)

def process_key_vigenere(key, string_length):
    expanded_key = key
    expanded_key_length = len(expanded_key)
    while expanded_key_length < string_length:
        expanded_key = expanded_key + key
        expanded_key_length = len(expanded_key)
    return(expanded_key)

def generate_full_vigenere_matrix():
    matrix = []
    for x in range(26):
        is_duplicate = True
        while is_duplicate:
            temp_alphabet = alphabet_uppercase
            random.shuffle(temp_alphabet)
            temp_string = ''.join(temp_alphabet)
            if temp_string not in matrix :
                is_duplicate = False
        matrix.append(temp_string)
    return matrix

full_vigenere_matrix = generate_full_vigenere_matrix()

def vigenere_full_encrypt(plaintext, key, full_vigenere_matrix):
    plaintext = process_input_vigenere(plaintext)
    key = process_input_vigenere(key)
    key = process_key_vigenere(key, len(plaintext))
    ciphertext = ''
    for i in range(len(plaintext)):
        idx_key = i % len(key)
        col = string.ascii_uppercase.index(plaintext[i])
        row = string.ascii_uppercase.index(key[idx_key])        
        ciphertext += full_vigenere_matrix[row][col]
    return ciphertext

def vigenere_full_decrypt(ciphertext, key, full_vigenere_matrix):
    ciphertext = regex.sub('', ciphertext.upper())
    key = regex.sub('', key.upper())
    plaintext = ''
    for i in range(len(ciphertext)):
        idx_key = i % len(key)
        row = string.ascii_uppercase.index(key[idx_key])
        vigenere_row = full_vigenere_matrix[row]
        letter_idx = vigenere_row.index(ciphertext[i])      
        plaintext += string.ascii_uppercase[letter_idx]
    return plaintext

a=(vigenere_full_encrypt("aku suka ayam", "komochan", full_vigenere_matrix))
print(a)
print(vigenere_full_decrypt(a, "komochan", full_vigenere_matrix))