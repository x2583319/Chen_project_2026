MAX_UNICODE = 1114112


def encrypt_letter(letter, key):
    """Encrypt one character using one key character."""
    encrypted_index = (ord(letter) + ord(key)) % MAX_UNICODE
    return chr(encrypted_index)


def decrypt_letter(letter, key):
    """Decrypt one character using one key character."""
    decrypted_index = (ord(letter) - ord(key)) % MAX_UNICODE
    return chr(decrypted_index)


def process_message(message, key, encrypt=True):
    """
    Encrypt or decrypt a full message using a repeating key.
    """
    if not key:
        raise ValueError("Key cannot be empty.")

    processed_letters = []

    for i, letter in enumerate(message):
        key_letter = key[i % len(key)]

        if encrypt:
            processed_letters.append(encrypt_letter(letter, key_letter))
        else:
            processed_letters.append(decrypt_letter(letter, key_letter))

    return "".join(processed_letters)


if __name__ == "__main__":
    message = "baby raccoon survived"
    key = "brainhack"

    encrypted_msg = process_message(message, key, encrypt=True)
    decrypted_msg = process_message(encrypted_msg, key, encrypt=False)

    print("Original:", message)
    print("Encrypted:", encrypted_msg)
    print("Decrypted:", decrypted_msg)

    if message == decrypted_msg:
        print("Test passed")
    else:
        print("Test failed")