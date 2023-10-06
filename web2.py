from flask import Flask, render_template, request, jsonify

from encryption import encrypt
from decryption import decrypt
from ascii_encryption import encrypt_string
from ascii_decryption import decrypt_string
from utils import binary_to_ascii
from force import *
from utils import ascii_to_binary




app = Flask(__name__)


# 加密函数
def f11(info, key):
    # 检查 info 是否为8位的二进制数字
    if not (len(info) == 8 and all(ch in ['0', '1'] for ch in info)):
        return "输入不合法: 信息必须为8位二进制数字"

    # 检查 key 是否为10位的二进制数字
    if not (len(key) == 10 and all(ch in ['0', '1'] for ch in key)):
        return "输入不合法: 密钥必须为10位二进制数字"

    return encrypt(info, key)

# 解密函数
def f12(info, key):
    # 检查 info 是否为8位的二进制数字
    if not (len(info) == 8 and all(ch in ['0', '1'] for ch in info)):
        return "输入不合法: 信息必须为8位二进制数字"

    # 检查 key 是否为10位的二进制数字
    if not (len(key) == 10 and all(ch in ['0', '1'] for ch in key)):
        return "输入不合法: 密钥必须为10位二进制数字"
    return decrypt(info, key)

def f21(info, key):

    # 检查 key 是否为10位的二进制数字
    if not (len(key) == 10 and all(ch in ['0', '1'] for ch in key)):
        return "输入不合法: 密钥必须为10位二进制数字"
    encrypted_string = encrypt_string(info, key)
    encrypted_ascii = binary_to_ascii(encrypted_string)


    return '加密后的二进制形式是'+encrypted_string +"\n"+'加密后的ASCLL码形式是'+encrypted_ascii

def f22(info, key):
    # 检查 key 是否为10位的二进制数字
    if not (len(key) == 10 and all(ch in ['0', '1'] for ch in key)):
        return "输入不合法: 密钥必须为10位二进制数字"
    info = ascii_to_binary(info)
    decrypted_string = decrypt_string(info, key)
    decrypted_ascii = binary_to_ascii(decrypted_string)
    return '解密后的二进制形式是'+decrypted_string +"\n"+'解密后的ASCLL码形式是'+decrypted_ascii

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/brute_force_page')
def brute_force_page():
    return render_template('index2.html')


@app.route('/brute_force', methods=['POST'])
def brute_force():

    data = request.json
    plaintext = data.get('username')
    ciphertext = data.get('password')


    # if not (len(plaintext) == 8  and all(ch in ['0', '1'] for ch in plaintext)):
    #     return jsonify({"message": "输入不合法:明文必须为8位二进制数字"})
    # if not (len(ciphertext) == 8 and all(ch in ['0', '1'] for ch in ciphertext)):
    #     return jsonify({"message": "输入不合法:密文必须为8位二进制数字"})

    decryptor = BruteForceDecrypt()
    result = decryptor.decrypt(plaintext, ciphertext)


    text1=str(result['single_thread'] )
    text2 = str(result['multi_thread'])

    return jsonify({"message": "单线程结果"+text1 +'\n'+'   '+'\n'
                               "多线程结果" + text2 + '\n'
                    })


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    info = data.get('username')
    key = data.get('password')
    option = data.get('option')

    operation = data.get('operation')
    if option == "binary":
        if operation == "encryption":
            result = f11(info, key)
            message = f"加密结果为: {result}"
        elif operation == "decryption":
            result = f12(info, key)
            message = f"解密结果为: {result}"
        else:
            return jsonify({"message": "无效的请求"}), 400
    elif option == "asciil":
        if operation == "encryption":
            result = f21(info, key)
            message = f"加密结果为: {result}"
        elif operation == "decryption":
            result = f22(info, key)
            message = f"解密结果为: {result}"
        else:
            return jsonify({"message": "无效的请求"}), 400
    else:
        return jsonify({"message": "无效的选项"}), 400

    return jsonify({"message": message})


if __name__ == '__main__':
    # app.run(host='10.234.113.9', port=6600, debug=True)
    app.run(port=6600, debug=True)
