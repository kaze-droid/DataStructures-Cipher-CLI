"""
AUTHOR: Ryan Yeo
STUDENT ID: 2214452
CLASS: DAAA/2B/01
"""

import string

class Caesar:
    def caesarCipher(self, text: str, key: int) -> str:
        """
        Encrypts/decrypts the text using the caesar cipher

        Parameters
        ----------
        text : str
            The text to be encrypted/decrypted
        key : int
            The key to be used for encryption/decryption
        """

        res = ""
        for char in text:
            if char.isalpha():
                if char.isupper():
                    base = ord('A')
                else:
                    base = ord('a')
                res+=chr(((ord(char)+key)-base)%26+base) 
            else:
                res+=char
        return res
    
    def printCaesarOutput(self, option: str, text: str, key: int, OFile: bool=False) -> None:
        """
        Prints the output of the caesar cipher either into the console or into a file

        Parameters
        ----------
        option : str
            'E' for encrypt, 'D' for decrypt
        text : str
            The text to be encrypted/decrypted
        key : int
            The key to be used for encryption/decryption
        OFile : bool, optional
            Whether the output is to a file, by default False
        """

        if OFile==False:
            if option == 'E':
                new_text = self.caesar(text, key)
                print(f"Plaintext:      {text}")
                print(f"Ciphertext:     {new_text}")
            
            else:
                new_text = self.caesar(text, -key)
                print(f"Ciphertext:     {text}")
                print(f"Plaintext:      {new_text}")
        else:
            output = self.getUserInput("Enter the output file name: ", "file", mode='w')
            print('\n')

            if option == 'E':
                new_text = self.caesar(text, key)
                with open(output, 'w') as f:
                    f.write(new_text)
            
            else:
                new_text = self.caesar(text, -key)
                with open(output, 'w') as f:
                    f.write(new_text)

    def calculateChiSquare(self, text_freq, master_freq):
        chi_squared = 0
        for letter in string.ascii_uppercase:
            observed = text_freq.get(letter, 0)
            expected = master_freq[letter]
            # Use chi-square formula
            chi_squared += ((observed - expected) ** 2) / expected
        return chi_squared

    def caesarBestShift(self, encrypted_text, master_freq):
        best_shift = None
        best_chi_squared = float('inf')

        for shift in range(26):
            # Shift the encrypted text by shift
            shifted_text = self.caesarCipher(encrypted_text.upper(), shift)
            # Calculate the frequency of each letter in percentage
            text_freq = {letter: shifted_text.count(letter) / len(shifted_text) for letter in string.ascii_uppercase}
            # Use Chi-Squared to compare the frequency of each letter in the shifted encrypted text to the master frequency
            chi_squared = self.calculateChiSquare(text_freq, master_freq)
            
            # Store lowest chi-squared value and its best-shift value
            if chi_squared < best_chi_squared:
                best_chi_squared = chi_squared
                best_shift = shift

        # Infered key for decrypting encrypted text will be 26 - shift for encrypted text
        return 26-best_shift