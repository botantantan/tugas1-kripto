from os import write


def padd_key(key, seq_input):
    pad_len = len(seq_input) - len(key)
    j = 0  #index of key
    output = [c for c in key]
    for i in range(pad_len):
        output += key[j]
        j += 1
        if (j == len(key)):
            j = 0
    return output

def process_key_vigenere_extended(key, string_length):
    expanded_key = key
    expanded_key_length = len(expanded_key)
    while expanded_key_length < string_length:
        expanded_key = expanded_key + key
        expanded_key_length = len(expanded_key)
    return(expanded_key)
    
def vigenere_extended_encrypt(plaintext, key):
    output = []
    key = process_key_vigenere_extended(key, len(plaintext))
    padded_key = padd_key(key, plaintext)
    for i in range(len(plaintext)):
        enc_ascii = (ord(plaintext[i]) + ord(padded_key[i])) % 256
        output.append(chr(enc_ascii))
    return ''.join(output)


def vigenere_extended_decrypt(encrypted, key):
    output = []
    key = process_key_vigenere_extended(key, len(encrypted))
    padded_key = padd_key(key, encrypted)
    for i in range(len(encrypted)):
        dec_ascii = (ord(encrypted[i]) - ord(padded_key[i])) % 256
        output.append(chr(dec_ascii))
    return ''.join(output)

# filepath = "test_file/img.jpg"
# inputFile = open(filepath, "rb")
# data = inputFile.read()
# data = data.decode("latin-1")
# inputFile.close()
# flag = True

# if (flag):
#     out = vigenere_extended_encrypt(data, "ayam")
# else:
#     out = vigenere_extended_decrypt(data, "ayam")

# out = out.encode("latin-1")
# outputFile = open(filepath, "wb")
# outputFile.write(out)
# outputFile.close()