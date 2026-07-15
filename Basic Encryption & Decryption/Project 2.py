def clean_keyword_shift(keyword_char):
    """
    Converts a keyword letter into its shift value (A=0, B=1, ... Z=25).
    We only ever pass uppercase letters into this from our functions below,
    so we don't need to worry about lowercase here.
    """
    return ord(keyword_char.upper()) - 65


def vigenere_encrypt(text, keyword):
    """
    Encrypts 'text' using the Vigenere cipher with the given 'keyword'.
    Unlike Caesar cipher, the shift amount changes for every letter,
    based on which keyword letter it currently lines up with.
    """
    result = ""
    keyword_index = 0  # tracks our position in the keyword (not in the message!)

    for char in text:
        if char.isupper():
            # Get the shift value from the current keyword letter
            shift = clean_keyword_shift(keyword[keyword_index % len(keyword)])
            # Same formula as Caesar cipher, just with a changing shift
            shifted = chr((ord(char) - 65 + shift) % 26 + 65)
            result += shifted
            keyword_index += 1  # move to the next keyword letter, only on a real letter

        elif char.islower():
            shift = clean_keyword_shift(keyword[keyword_index % len(keyword)])
            shifted = chr((ord(char) - 97 + shift) % 26 + 97)
            result += shifted
            keyword_index += 1

        else:
            # Spaces, punctuation, numbers pass through untouched
            # Crucially, we do NOT increment keyword_index here,
            # otherwise the keyword would desync from the letters
            result += char

    return result


def vigenere_decrypt(text, keyword):
    """
    Decrypts text encrypted with vigenere_encrypt().
    Exactly the same logic, but we SUBTRACT the shift instead of adding it.
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


# ---- Main program ----

message = input("Enter your message to encrypt: ")
keyword = input("Enter your keyword (letters only, e.g. KEY): ")

encrypted_message = vigenere_encrypt(message, keyword)
decrypted_message = vigenere_decrypt(encrypted_message, keyword)

print("\nOriginal Message :", message)
print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)