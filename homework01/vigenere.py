charvalue = {
    "A": 0,
    "a": 0,
    "B": 1,
    "b": 1,
    "C": 2,
    "c": 2,
    "D": 3,
    "d": 3,
    "E": 4,
    "e": 4,
    "F": 5,
    "f": 5,
    "G": 6,
    "g": 6,
    "H": 7,
    "h": 7,
    "I": 8,
    "i": 8,
    "J": 9,
    "j": 9,
    "K": 10,
    "k": 10,
    "L": 11,
    "l": 11,
    "M": 12,
    "m": 12,
    "N": 13,
    "n": 13,
    "O": 14,
    "o": 14,
    "P": 15,
    "p": 15,
    "Q": 16,
    "q": 16,
    "R": 17,
    "r": 17,
    "S": 18,
    "s": 18,
    "T": 19,
    "t": 19,
    "U": 20,
    "u": 20,
    "V": 21,
    "v": 21,
    "W": 22,
    "w": 22,
    "X": 23,
    "x": 23,
    "Y": 24,
    "y": 24,
    "Z": 25,
    "z": 25,
}


def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    # PUT YOUR CODE HERE
    p_list = list(plaintext)
    k_list = list(keyword)
    i = 0
    j = 0
    while i < len(plaintext):
        if j == len(keyword):
            j = 0
        if p_list[i].isalpha():
            if (
                ord(p_list[i]) + charvalue[k_list[j]] > 90
                and ord(p_list[i]) < 91
                or ord(p_list[i]) + charvalue[k_list[j]] > 122
                and ord(p_list[i]) < 123
            ):
                p_list[i] = chr((ord(p_list[i]) + charvalue[k_list[j]]) - 26)
            else:
                p_list[i] = chr(ord(p_list[i]) + charvalue[k_list[j]])
        i = i + 1
        j = j + 1
    ciphertext = "".join(p_list)
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    # PUT YOUR CODE HERE
    p_list = list(ciphertext)
    k_list = list(keyword)
    i = 0
    j = 0
    while i < len(ciphertext):
        if j == len(keyword):
            j = 0
        if p_list[i].isalpha():
            if (
                ord(p_list[i]) - charvalue[k_list[j]] < 65
                or ord(p_list[i]) - charvalue[k_list[j]] < 97
                and ord(p_list[i]) > 96
            ):
                p_list[i] = chr(26 + (ord(p_list[i]) - charvalue[k_list[j]]))
            else:
                p_list[i] = chr(ord(p_list[i]) - charvalue[k_list[j]])
        i = i + 1
        j = j + 1
    plaintext = "".join(p_list)
    return plaintext


# print(encrypt_vigenere("abcdef", "bc"))
