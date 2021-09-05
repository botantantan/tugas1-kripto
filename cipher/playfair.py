import string
import itertools
import re
 
def chunker(seq, size):
    it = iter(seq)
    while True:
        chunk = tuple(itertools.islice(it, size))
        if not chunk:
            return
        yield chunk
 
def process_input_playfair(input):
    input = "".join([c.upper() for c in input if c in string.ascii_letters])
    input = re.sub(r"[J]", 'I', input)

    return(input)
 
def prepare_input(dirty):
    dirty = process_input_playfair(dirty)
    clean = ""
    if len(dirty) < 2:
        return dirty
    for i in range(len(dirty) - 1):
        clean += dirty[i] 
        if dirty[i] == dirty[i + 1]:
            clean += "X"
    clean += dirty[-1]
    if len(clean) & 1:
        clean += "X"
    return clean
 
 
def generate_table(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    table = []
    key=prepare_input(key)
    for char in key:
        if char not in table and char in alphabet:
            table.append(char)
    for char in alphabet:
        if char not in table:
            table.append(char)
    return table
 
 
def playfair_encrypt(plaintext, key):
    table = generate_table(key)
    plaintext = prepare_input(plaintext)
    encrypted = ""
 
    for char1, char2 in chunker(plaintext, 2):
        row1, col1 = divmod(table.index(char1), 5)
        row2, col2 = divmod(table.index(char2), 5)
 
        if row1 == row2:
            encrypted += table[row1 * 5 + (col1 + 1) % 5]
            encrypted += table[row2 * 5 + (col2 + 1) % 5]
        elif col1 == col2:
            encrypted += table[((row1 + 1) % 5) * 5 + col1]
            encrypted += table[((row2 + 1) % 5) * 5 + col2]
        else:  
            encrypted += table[row1 * 5 + col2]
            encrypted += table[row2 * 5 + col1]
 
    return encrypted
 
 
def playfair_decrypt(ciphertext, key):
    table = generate_table(key)
    ciphertext = prepare_input(ciphertext)
    decrypted = ""
 
    for char1, char2 in chunker(ciphertext, 2):
        row1, col1 = divmod(table.index(char1), 5)
        row2, col2 = divmod(table.index(char2), 5)
 
        if row1 == row2:
            decrypted += table[row1 * 5 + (col1 - 1) % 5]
            decrypted += table[row2 * 5 + (col2 - 1) % 5]
        elif col1 == col2:
            decrypted += table[((row1 - 1) % 5) * 5 + col1]
            decrypted += table[((row2 - 1) % 5) * 5 + col2]
        else:  
            decrypted += table[row1 * 5 + col2]
            decrypted += table[row2 * 5 + col1]

    decrypted = re.sub(r"[X]", '', decrypted)
    return decrypted