import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    # PUT YOUR CODE HERE
    if len(list(plaintext)) > 0:
        a_list = list(plaintext)
        i = 0
        while i < len(a_list):
            if a_list[i].isalpha():
                if (
                    ord(a_list[i]) + shift > 90
                    and ord(a_list[i]) < 91
                    or ord(a_list[i]) + shift > 122
                    and ord(a_list[i]) < 123
                ):
                    a_list[i] = chr((ord(a_list[i]) + shift) - 26)
                else:
                    a_list[i] = chr(ord(a_list[i]) + shift)
            ciphertext = "".join(a_list)
            i = i + 1
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    # PUT YOUR CODE HERE
    if len(list(ciphertext)) > 0:
        a_list = list(ciphertext)
        i = 0
        while i < len(a_list):
            if a_list[i].isalpha():
                if (
                    ord(a_list[i]) - shift < 65
                    or ord(a_list[i]) - shift < 97
                    and ord(a_list[i]) > 96
                ):
                    a_list[i] = chr(26 + (ord(a_list[i]) - shift))
                else:
                    a_list[i] = chr(ord(a_list[i]) - shift)
            plaintext = "".join(a_list)
            i = i + 1
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
