import string

def euclidean(a, b):
	x,y, u,v = 0,1, 1,0
	while a != 0:
		q, r = b//a, b%a
		m, n = x-u*q, y-v*q
		b,a, x,y, u,v = a,r, u,v, m,n
	gcd = b
	return gcd, x, y

def modular_inverse(a, m):
	gcd, x, y = euclidean(a, m)
	if gcd != 1:
		return None
	else:
		return x % m

def process_input_affine(input):
    input = "".join([c.upper() for c in input if c in string.ascii_letters])
    return(input)
 
def affine_encrypt(plaintext, key_m, key_b):
	plaintext= process_input_affine(plaintext)
	encrypted = ''.join([ chr((( key_m*(ord(t) - ord('A')) + key_b ) % 26)
				+ ord('A')) for t in plaintext ])
	return encrypted


def affine_decrypt(ciphertext, key_m, key_b):
	ciphertext= process_input_affine(ciphertext)
	decrypted = ''.join([ chr((( modular_inverse(key_m, 26)*(ord(c) - ord('A') - key_b))
					% 26) + ord('A')) for c in ciphertext ])
	return decrypted