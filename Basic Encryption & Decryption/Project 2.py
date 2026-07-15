#Basic Encryption & Decryption using Caesar Cipher and Vigenère Cipher:
def clean_keyword_shift(keyword_char):
    return ord(keyword_char.upper()) - 65


def vigenere_encrypt(text, keyword):
    result = ""
    keyword_index = 0  

    for char in text:
        if char.isupper():
            shift = clean_keyword_shift(keyword[keyword_index % len(keyword)])
            shifted = chr((ord(char) - 65 + shift) % 26 + 65)
            result += shifted
            keyword_index += 1  

        elif char.islower():
            shift = clean_keyword_shift(keyword[keyword_index % len(keyword)])
            shifted = chr((ord(char) - 97 + shift) % 26 + 97)
            result += shifted
            keyword_index += 1

        else:
            result += char

    return result


def vigenere_decrypt(text, keyword):
    """
    Decrypts text encrypted 
    """
    result = ""
    keyword_index = 0

    for char in text:
        if char.isupper():
            shift = clean_keyword_shift(keyword[keyword_index % len(keyword)])
            shifted = chr((ord(char) - 65 - shift) % 26 + 65)
            result += shifted
            keyword_index += 1

        elif char.islower():
            shift = clean_keyword_shift(keyword[keyword_index % len(keyword)])
            shifted = chr((ord(char) - 97 - shift) % 26 + 97)
            result += shifted
            keyword_index += 1

        else:
            result += char

    return result

message = input("Enter your message to encrypt: ")
keyword = input("Enter your keyword (letters only, e.g. KEY): ")

encrypted_message = vigenere_encrypt(message, keyword)
decrypted_message = vigenere_decrypt(encrypted_message, keyword)

print("\nOriginal Message :", message)
print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)