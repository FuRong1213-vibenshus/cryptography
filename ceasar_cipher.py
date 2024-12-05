
alphabet = "abcdefghijklmnopqrstuvwxyz"
def ceasar_cipher(msg, key):
    cipher_msg = ""
    for i in msg:
        print(str2:int(i))
        new_index = (alphabet.index(i)+key)%26
        cipher_msg += alphabet[new_index]

    return cipher_msg

print(ceasar_cipher("hello",3))

