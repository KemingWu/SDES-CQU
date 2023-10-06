from utils import *


# Encrypt plaintext using S-DES
def encrypt(plaintext, key):
    key1, key2 = generate_subkeys(key, PERMUTATION_P10, PERMUTATION_P8)

    # Initial permutation
    plaintext = permute(plaintext, INITIAL_PERMUTATION)
    # l0 = p[:4]
    # r0 = p[4:]
    # l1 = r0

    left_half = plaintext[:4]
    right_half = plaintext[4:]
    left_previous = right_half

    # First round
    f_result = f_function(right_half, key1, SBOX0, SBOX1, PERMUTATION_P4)
    right_half1_int = int(left_half, 2) ^ int(f_result, 2)
    right_half1 = format(right_half1_int, '04b')

    # Second round
    f_result = f_function(right_half1, key2, SBOX0, SBOX1, PERMUTATION_P4)
    right_half2_int = int(left_previous, 2) ^ int(f_result, 2)
    right_half2 = format(right_half2_int, '04b')

    # Final permutation
    return permute(right_half2 + right_half1, INVERSE_INITIAL_PERMUTATION)
