"""
AUTHOR: Ryan Yeo
STUDENT ID: 2214452
CLASS: DAAA/2B/01
"""

from Utils.Ciphers.Caesar import Caesar
from Utils.Ciphers.Enigma import Enigma
from Utils.Ciphers.Vigenere import Vigenere

class Ciphers():
    """
    This class contains the cipher objects
    """
    def __init__(self):
        self.Caesar = Caesar()
        self.Vigenere = Vigenere()
        self.Enigma = Enigma()