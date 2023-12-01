"""
AUTHOR: Ryan Yeo
STUDENT ID: 2214452
CLASS: DAAA/2B/01
"""

class Keyboard:
    # Converts a keyboard input into a signal
    def keyboardForward(self, letter:str) -> int:
        signal = ord(letter.upper()) - ord('A')
        return signal
    
    # Converts a signal back into a keyboard output
    def keyboardBackward(self, signal: int) -> str:
        letter = chr(signal + ord('A'))
        return letter
    