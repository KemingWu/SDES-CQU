# Permutation tables
PERMUTATION_P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
PERMUTATION_P8 = [6, 3, 7, 4, 8, 5, 10, 9]
PERMUTATION_P4 = [2, 4, 3, 1]
INITIAL_PERMUTATION = [2, 6, 3, 1, 4, 8, 5, 7]
EXPANSION_PERMUTATION = [4, 1, 2, 3, 2, 3, 4, 1]
INVERSE_INITIAL_PERMUTATION = [4, 1, 3, 5, 7, 2, 8, 6]

# S-boxes
SBOX0 = [
    [1, 0, 3, 2],
    [3, 2, 1, 0],
    [0, 2, 1, 3],
    [3, 1, 0, 2]
]
SBOX1 = [
    [0, 1, 2, 3],
    [2, 3, 1, 0],
    [3, 0, 1, 2],
    [2, 1, 0, 3]
]

KEY_LENGTH = 10
DATA_LENGTH = 8


# Perform a permutation
def permute(input_str, permutation_table):
    output_str = ''
    for bit_position in permutation_table:
        output_str += input_str[bit_position - 1]
    return output_str


# Perform a left shift
def left_shift(key, n):
    left_half = key[:5]
    right_half = key[5:]
    shifted_left = left_half[n:] + left_half[:n]
    shifted_right = right_half[n:] + right_half[:n]
    return shifted_left + shifted_right


# Generate subkeys
def generate_subkeys(key, p10_table, p8_table):
    p10_key = permute(key, p10_table)
    key1 = permute(left_shift(p10_key, 1), p8_table)
    key2 = permute(left_shift(left_shift(p10_key, 1), 1), p8_table)
    return key1, key2


# The function used in the Fk function
def f_function(right_half, subkey, sbox0, sbox1, p4_table):
    # Expansion and XOR
    expanded = permute(right_half, EXPANSION_PERMUTATION)
    xored = int(expanded, 2) ^ int(subkey, 2)
    xored_str = format(xored, '08b')

    # S-box substitutions
    s0_input = xored_str[:4]
    s1_input = xored_str[4:]
    s0_row = int(s0_input[0] + s0_input[3], 2)
    s0_col = int(s0_input[1:3], 2)
    s1_row = int(s1_input[0] + s1_input[3], 2)
    s1_col = int(s1_input[1:3], 2)
    s0_output = format(sbox0[s0_row][s0_col], '02b')
    s1_output = format(sbox1[s1_row][s1_col], '02b')
    s_output = s0_output + s1_output

    # Permutation
    return permute(s_output, p4_table)


# ASCII to Binary
def ascii_to_binary(ascii_string):
    binary_string = ""
    for character in ascii_string:
        # 使用ord函数获取字符的ASCII码，然后使用bin函数将其转换为二进制
        binary_string += bin(ord(character))[2:].zfill(8)  # 使用zfill在左侧填充0，以确保每个字符都转换为8位二进制数
    return binary_string


# Binary to ASCII
def binary_to_ascii(binary_string):
    ascii_string = ""
    for i in range(0, len(binary_string), 8):  # 每8位一组
        # 使用int函数将二进制数据转换为整数（即ASCII码），然后使用chr函数将其转换为字符
        ascii_string += chr(int(binary_string[i:i + 8], 2))
    return ascii_string
