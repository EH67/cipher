#chr65-90 is A-Z
import random

def known_key_encoding(plaintext, shift):
    for i in plaintext.upper().strip():
        print(chr((ord(i) + shift - 65) % 26 + 65), end='')
def random_encoding(plaintext):
    shift = random.randint(1,100)
    print('shift of {}'.format(shift))
    for i in plaintext.upper().strip():
        print(chr((ord(i) + shift - 65) % 26 + 65), end = '')

def known_key_decoding(ciphertext, shift):
    for i in ciphertext.upper().strip():
        print(chr((ord(i) + shift - 65) % 26 + 65), end = '')

def unknown_key_decoding(ciphertext): #uses brute force
    for j in range(26):
        for i in ciphertext.upper().strip():
            print(chr((ord(i) + j - 65) % 26 + 65), end='')
        print('\n')

unknown_key_decoding_brute_force('bqqmf')