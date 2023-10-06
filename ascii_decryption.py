from decryption import decrypt


def decrypt_string(encrypted_string, key):
    # 初始化解密结果
    decrypted_string = ""
    # 每8位一组进行解密
    for i in range(0, len(encrypted_string), 8):
        ciphertext = encrypted_string[i:i + 8]
        plaintext = decrypt(ciphertext, key)
        decrypted_string += plaintext
    return decrypted_string


# # 测试
# encrypted_string = "01110011011010010110101101101001"
# key = "1010000010"
# decrypted_string = decrypt_string(encrypted_string, key)
# print(decrypted_string)
