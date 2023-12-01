"""
AUTHOR: Ryan Yeo
STUDENT ID: 2214452
CLASS: DAAA/2B/01
"""

import string
# A reflector is very similar to a rotor except for the fact that it does not contain a turnover notch so it does not rotate
class Reflector:
    def __init__(self, reflectorType: str = 'UKW-B'):
        self.__right = string.ascii_uppercase
        # Swapped contains the wiring for each rotor which is used to encrypt the signal once
        self.__left = self.getReflectorWiring(reflectorType)
    
    def getReflectorWiring(self, reflectorType: str) -> str:
        # For this assignment, we will be using the original Enigma I Model (so the Reflector options only include: UKW-A, UKW-B, UKW-C)
        if reflectorType not in ["UKW-A", "UKW-B", "UKW-C"]:
            raise ValueError("Reflector Type must be either 'UKW-A', 'UKW-B' or 'UKW-C'")

        # The wiring used can be found on en.wikiperdia.org/wiki/Enigma_rotor_details#Rotor_wiring_tables
        if reflectorType == "UKW-A":
            wiring = "EJMZALYXVBWFCRQUONTSPIKHGD"
        elif reflectorType == "UKW-B":
            wiring = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
        elif reflectorType == "UKW-C":
            wiring = "FVPJIAOYEDRZXWGCTKUQSBNMHL"
        
        return wiring
    
    def reflect(self, inputSignal: int) -> int:
        # Convert signal to letter from the left keys
        letter = self.__left[inputSignal]
        # Convert letter to signal using the right keys
        outputSignal = self.__right.index(letter)
        return outputSignal