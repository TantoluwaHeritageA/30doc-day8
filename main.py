# Task 1
def encrypt_text(text, shift):
    text = text.lower()
    print("Plain text: ", text)
    encryption = ""
    for el in text:
        el_index = ord(el) - ord('a')
        # print(el_index)
        crypt = (el_index + shift) % 26
        # print(crypt)
        crypt_char = chr(crypt + ord('a'))
        # print(crypt_char)
        encryption = encryption + crypt_char
    print('Encrypted text:', encryption)


encrypt_text("python", 5)


# Task 2
def decrypt_text(encrypt_text, shift):
    plain_text = ""
    print("Encrypted text: ", encrypt_text)
    for el in encrypt_text:
        el_index = ord(el) - ord('a')
        decrypt = (el_index - shift) % 26
        # print(crypt)
        decrypt_char = chr(decrypt + ord('a'))
        # print(crypt_char)
        plain_text = plain_text + decrypt_char
    print('Decrypted text:', plain_text)


decrypt_text("udymts", 5)

# Task 3


def check_encrypt(characters, shift, check_text):
    characters = characters.lower()
    if check_text == True:
        encoded = encrypt_text(characters, shift)
        return encoded
    else:
        decoded = decrypt_text(characters, shift)
        return decoded


print(check_encrypt("string", 5, False))
