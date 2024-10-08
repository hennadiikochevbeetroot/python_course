def caesar_cipher(plain_text: str, shift: int) -> str:
    ALPHABET_LENGTH = 26
    cipher_text = ""
    for char in plain_text:
        if char.isalpha():
            # Determine the offset based on the shift value
            offset = ord('a') if char.islower() else ord('A')
            # Apply the shift to the character and wrap around if necessary
            # abc, k=2
            #
            # offset = 97
            # ascii_code_number = (97 - 97 + 2) % 26 + 97 = 2 + 97 = 99

            ascii_code_number = (ord(char) - offset + shift) % ALPHABET_LENGTH + offset

            cipher_char = chr(ascii_code_number)
            cipher_text += cipher_char
        else:
            # Leave non-alphabetic characters unchanged
            cipher_text += char

    return cipher_text
