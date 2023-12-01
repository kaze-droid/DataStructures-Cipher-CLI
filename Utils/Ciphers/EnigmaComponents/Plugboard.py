"""
AUTHOR: Ryan Yeo
STUDENT ID: 2214452
CLASS: DAAA/2B/01
"""

import string

class Plugboard():
    def __init__(self, pairs: list[str] = []):
        self.__right = string.ascii_uppercase
        self.__left = string.ascii_uppercase
        for pair in pairs:
            l = pair[0].upper()
            r = pair[1].upper()
            pos_l = ord(l) - ord('A')
            pos_r = ord(r) - ord('A')
            # Replace l with r
            self.__right = self.__right[:pos_l] + r + self.__right[pos_l+1:]
            # Replace r with l
            self.__right = self.__right[:pos_r] + l + self.__right[pos_r+1:]

    def plugboardForward(self, leftSignal: int) -> int:
        # Convert signal to letter from the left keys
        letter = self.__left[leftSignal]
        # Convert letter to signal using the right keys
        rightSignal = self.__right.index(letter)
        return rightSignal
    
    def plugboardBackward(self, rightSignal: int) -> int:
        # Convert signal to letter from the right keys
        letter = self.__right[rightSignal]
        # Convert letter to signal using the left keys
        leftSignal = self.__left.index(letter)
        return leftSignal
        