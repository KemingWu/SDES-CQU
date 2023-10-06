from utils import *
from encryption import encrypt


def encrypt_string(ascii_string, key):
    # 将ASCII字符串转换为二进制数据
    binary_string = ascii_to_binary(ascii_string)
    # 初始化加密结果
    encrypted_string = ""
    # 每8位一组进行加密
    for i in range(0, len(binary_string), 8):
        plaintext = binary_string[i:i + 8]
        ciphertext = encrypt(plaintext, key)
        encrypted_string += ciphertext
    return encrypted_string
