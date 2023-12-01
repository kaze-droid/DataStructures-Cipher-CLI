"""
AUTHOR: Ryan Yeo
STUDENT ID: 2214452
CLASS: DAAA/2B/01
"""

from Utils.IO.GetInput import GetInput

class DisplayOutput(GetInput):
    def __init__(self):
        super(DisplayOutput, self).__init__()
    def printCaesarOutput(self, option: str, text: str, new_text: str, key: int, OFile: bool=False) -> None:
        """
        Prints the output of the caesar cipher either into the console or into a file

        Parameters
        ----------
        option : str
            'E' for encrypt, 'D' for decrypt
        text : str
            The text to be encrypted/decrypted
        new_text : str
            The encrypted/decrypted text
        key : int
            The key to be used for encryption/decryption
        OFile : bool, optional
            Whether the output is to a file, by default False
        """

        if OFile==False:
            if option == 'E':
                print(f"Plaintext:      {text}")
                print(f"Ciphertext:     {new_text}")
            
            else:
                print(f"Ciphertext:     {text}")
                print(f"Plaintext:      {new_text}")

        else:
            output = self.getUserInput("Enter the output file name: ", "file", mode='w')
            print('\n')

            if option == 'E':
                with open(output, 'w') as f:
                    f.write(new_text)
            
            else:
                with open(output, 'w') as f:
                    f.write(new_text)