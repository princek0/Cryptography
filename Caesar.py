def caesar(plain_text, key):  # Caesar cipher function.
    plain_text = plain_text.lower()
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]
    for i in plain_text:
        if i not in alphabet:
            pass
        else:
            plain_text = plain_text.replace(i, alphabet[
                (alphabet.index(i) + key) % 26])  # Mod 26 needed to loop back around the alphabet.
    return plain_text


def de_caesar(cipher_text, key):  # De-ciphers the cipher with a known key.
    cipher_text = cipher_text.lower()
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]
    for i in cipher_text:
        if i not in alphabet:
            pass
        else:
            cipher_text = cipher_text.replace(i, alphabet[
                (alphabet.index(i) - key) % 26])  # Mod 26 needed to loop back around the alphabet.
    return cipher_text
