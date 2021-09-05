import string
import numpy as np

def process_input_hill(input):
    input = "".join([c.upper() for c in input if c in string.ascii_letters])
    return(input)

def check_length_hill(input):
    if len(input)%2 != 0:
        input += "0"

def find_multiplicative_inverse(determinant):
    multiplicative_inverse = -1
    for i in range(26):
        inverse = determinant * i
        if inverse % 26 == 1:
            multiplicative_inverse = i
            break
    return multiplicative_inverse

def make_key(key):
    determinant = 0
    C = None
    while True:
        C = create_matrix_of_integers_from_string(key)
        determinant = C[0][0] * C[1][1] - C[0][1] * C[1][0]
        determinant = determinant % 26
        inverse_element = find_multiplicative_inverse(determinant)
        if inverse_element == -1:
            print("Determinant is not relatively prime to 26, uninvertible key")
        elif np.amax(C) > 26 and np.amin(C) < 0:
            print("Only a-z characters are accepted")
            print(np.amax(C), np.amin(C))
        else:
            break
    return C

def create_matrix_of_integers_from_string(string):
    integers = [char_to_int(c) for c in string]
    length = len(integers)
    M = np.zeros((2, int(length / 2)), dtype=np.int32)
    iterator = 0
    for column in range(int(length / 2)):
        for row in range(2):
            M[row][column] = integers[iterator]
            iterator += 1
    return M

def char_to_int(char):
    char = char.upper()
    integer = ord(char) - 65
    return integer

def find_inverse(C):
    determinant = C[0][0] * C[1][1] - C[0][1] * C[1][0]
    determinant = determinant % 26
    multiplicative_inverse = find_multiplicative_inverse(determinant)
    C_inverse = C
    C_inverse[0][0], C_inverse[1][1] = C_inverse[1, 1], C_inverse[0, 0]
    C[0][1] *= -1
    C[1][0] *= -1
    for row in range(2):
        for column in range(2):
            C_inverse[row][column] *= multiplicative_inverse
            C_inverse[row][column] = C_inverse[row][column] % 26
    return C_inverse

def hill_encrypt(plaintext, key):
    plaintext = process_input_hill(plaintext)
    C = make_key(key)
    check_length_hill(plaintext);
    P = create_matrix_of_integers_from_string(plaintext)
    string_length = int(len(plaintext) / 2)
    encrypted = ""
    for i in range(string_length):
        row_0 = P[0][i] * C[0][0] + P[1][i] * C[0][1]
        integer = int(row_0 % 26 + 65)
        encrypted += chr(integer)
        row_1 = P[0][i] * C[1][0] + P[1][i] * C[1][1]
        integer = int(row_1 % 26 + 65)
        encrypted += chr(integer)
    return encrypted

def hill_decrypt(ciphertext, key):
    C = make_key(key)
    C_inverse = find_inverse(C)
    P = create_matrix_of_integers_from_string(ciphertext)
    string_length = int(len(ciphertext) / 2)
    decrypted = ""
    for i in range(string_length):
        column_0 = P[0][i] * C_inverse[0][0] + P[1][i] * C_inverse[0][1]
        integer = int(column_0 % 26 + 65)
        decrypted += chr(integer)
        column_1 = P[0][i] * C_inverse[1][0] + P[1][i] * C_inverse[1][1]
        integer = int(column_1 % 26 + 65)
        decrypted += chr(integer)
    if decrypted[-1] == "0":
        decrypted = decrypted[:-1]
    return decrypted
