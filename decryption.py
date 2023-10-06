from utils import *


# Decrypt ciphertext using S-DES
def decrypt(ciphertext, key):
    key1, key2 = generate_subkeys(key, PERMUTATION_P10, PERMUTATION_P8)

    # Initial permutation
    ciphertext = permute(ciphertext, INITIAL_PERMUTATION)

    # r2 = c[:4]
    # l2 = c[4:]

    right_previous = ciphertext[:4]
    left_previous = ciphertext[4:]

    # First round
    f_result = f_function(left_previous, key2, SBOX0, SBOX1, PERMUTATION_P4)
    left_half1_int = int(right_previous, 2) ^ int(f_result, 2)
    left_half1 = format(left_half1_int, '04b')

    # Second round
    f_result = f_function(left_half1, key1, SBOX0, SBOX1, PERMUTATION_P4)
    right_half1_int = int(left_previous, 2) ^ int(f_result, 2)
    right_half1 = format(right_half1_int, '04b')

    # Final permutation
    return permute(right_half1 + left_half1, INVERSE_INITIAL_PERMUTATION)
