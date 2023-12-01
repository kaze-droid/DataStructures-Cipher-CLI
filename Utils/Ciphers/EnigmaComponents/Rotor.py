"""
AUTHOR: Ryan Yeo
STUDENT ID: 2214452
CLASS: DAAA/2B/01
"""

import string
class Rotor:
    def __init__(self, rotorType: str = 'I'):
        self.__right = string.ascii_uppercase
        # Swapped contains the wiring for each rotor which is used to encrypt the signal once
        # Notch contains the turnover notch for each rotor which is the condition for the next rotor to rotate (i.e. changing the encryption for the same letter)
        self.__left, self.__notch = self.getRotorWiring(rotorType)
    
    def getRotorWiring(self, rotorType: str) -> "tuple(str, str)":
        # For this assignment, we will be using the original Enigma I Model (so the Rotor options only include: I, II, III, IV, V)
        if rotorType not in ["I", "II", "III", "IV", "V"]:
            raise ValueError("Rotor Type must be either 'I', 'II', 'III', 'IV' or 'V'")

        # The wiring used can be found on en.wikiperdia.org/wiki/Enigma_rotor_details#Rotor_wiring_tables
        # The notches used can be found on en.wikiperdia.org/wiki/Enigma_rotor_details#Turnover_notch_positions
        if rotorType == "I":
            wiring = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
            notch = "Q"
        elif rotorType == "II":
            wiring = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
            notch = "E"
        elif rotorType == "III":
            wiring = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
            notch = "V"
        elif rotorType == "IV":
            wiring = "ESOVPZJAYQUIRHXLNFTGKDCMWB"
            notch = "J"
        elif rotorType == "V":
            wiring = "VZBRGITYUPSDNHLXAWMJQOFECK"
            notch = "Z"
        
        return (wiring, notch)
    
    def rotorForward(self, leftSignal: int) -> int:
        # Convert signal to letter from the left keys
        letter = self.__left[leftSignal]
        # Convert letter to signal using right keys
        rightSignal = self.__right.index(letter)
        return rightSignal

    def rotorBackward(self, rightSignal: int) -> int:
        # Convert signal to letter from the right keys
        letter = self.__right[rightSignal]
        # Convert letter to signal using left keys
        leftSignal = self.__left.index(letter)
        return leftSignal
    
    def rotate(self, rotations: int = 1, forward: bool = True):
        """
        Rotates the rotor by the specified number of steps

        Parameters
        ----------
        rotations : int, optional
            The number of steps to rotate, by default 1
        forward : bool, optional
            Whether to rotate forward or backward, by default True
        """
        for rotation in range(rotations):
            if forward:
                # Rotate the rotor by 1 step forward
                self.__right = self.__right[1:] + self.__right[0]
                self.__left = self.__left[1:] + self.__left[0]
            else:
                # Rotate the rotor by 1 step backward
                self.__right = self.__right[25] + self.__right[:25]
                self.__left = self.__left[25] + self.__left[:25]
    
    def rotateToLetter(self, letter: str):
        rotations = self.__right.index(letter)
        self.rotate(rotations)
    
    def setRing(self, ring: int):
        # Rotate the rotor backwards
        # -1 because ring was historically 1-indexed
        self.rotate(ring-1, forward=False)

        # Adjust the turnover notch in relation to the wiring
        n_notch = string.ascii_uppercase.index(self.__notch)
        self.setNotch(string.ascii_uppercase[(n_notch-ring)%26])
        

    def getWires(self):
        return self.__right, self.__left

    def getNotch(self):
        return self.__notch
    
    def setNotch(self, notch):
        self.__notch = notch

    def __str__(self):
        return f"Rotor({self.__left}, {self.__notch})"