"""
AUTHOR: Ryan Yeo
STUDENT ID: 2214452
CLASS: DAAA/2B/01
"""

import string
from Utils.Ciphers.Caesar import Caesar

class Vigenere:
    def __init__(self):
        super(Vigenere, self).__init__()
        self.__caesar = Caesar()
    

    def vigenereCipher(self, message: str, key: str, encrypt: bool = True) -> str:
        """
        Encrypts/decrypts the message using the vigenere cipher

        Parameters
        ----------
        message : str
            The message to be encrypted/decrypted
        key : str
            The key to be used for encryption/decryption
        encrypt : bool, optional
            Whether to encrypt or decrypt, by default True
        
        Returns
        -------
        str
            The encrypted/decrypted message
        """
        lengthened_key = []
        num_zeros = 0
        for i, char in enumerate(message):
            if char not in string.ascii_letters:
                # If the character is not a letter, add a 0 to the key
                lengthened_key.append(0)
                num_zeros += 1
            else:
                index = max(i - num_zeros, 0)
                lengthened_key.append(self.letterToIndex(key[index % len(key)]))
                

        new_text = ""
        # Encrypt the message with the lengthened key
        for l, k in zip(message, lengthened_key):
                if encrypt:
                    new_text += self.__caesar.caesarCipher(l, k)
                else:
                    new_text += self.__caesar.caesarCipher(l, -k)
        
        return new_text
        

    
    def letterToIndex(self, letter: str) -> int:
        """
        Converts a letter to its index in the alphabet

        Parameters
        ----------
        letter : str
            The letter to be converted
        
        Returns
        -------
        int
            The index of the letter in the alphabet
        """
        if letter in string.ascii_lowercase:
            return string.ascii_lowercase.index(letter)
        elif letter in string.ascii_uppercase:
            return string.ascii_uppercase.index(letter)
        else:
            raise ValueError("Letter is not in the alphabet")
            