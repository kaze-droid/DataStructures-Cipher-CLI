"""
AUTHOR: Ryan Yeo
STUDENT ID: 2214452
CLASS: DAAA/2B/01
"""

from Utils.Ciphers.EnigmaComponents.Keyboard import Keyboard
from Utils.Ciphers.EnigmaComponents.Plugboard import Plugboard
from Utils.Ciphers.EnigmaComponents.Rotor import Rotor
from Utils.Ciphers.EnigmaComponents.Reflector import Reflector

class Enigma(Keyboard, Plugboard, Rotor, Reflector):
    """
    This class contains the Enigma machine
    It inherits from the Keyboard, Plugboard, Rotor and Reflector classes
    Reflector: e.g. A
        The reflector is quite similar to a rotor in that it is used to encrypt a letter e.g. A is encrypted to F. However, the reflector is used to encrypt the letter again after it has been encrypted by the rotors. In an enigma machine, there is only one reflector
    Rotor: e.g. I, II, III
        The rotor is used to encrypt a letter e.g. A is encrypted to F. In an enigma machine, there are three different rotors which are then connected to a reflector. Each time a key is pressed, one of the rotor turns and thus the encryption for the same letter changes
    Starting Position of Rotor: e.g. A, A, A
        The starting position of the rotor is used to set the starting position of the rotors. In an enigma machine, there are three rotors and thus three starting positions
    Plugboard: e.g. A-R, G-K, O-X
        The plugboard is used to switch two letters encryption e.g. A is encrypted to F and R is encrypted to B, then using a plugboard connnecting A-R would result in A being encrypted to B and R being encrypted to F
    Ring Settings: e.g. 1, 1, 1
        The ring settings are used to set the starting position of the rotors. In an enigma machine, there are three rotors and thus three ring settings
    """
    def __init__(self):
        # Initialise all classes one by one
        self.__kb = Keyboard()
        self.__pb = None
        self.__rotor1 = None
        self.__rotor2 = None
        self.__rotor3 = None
        self.__reflector = None

    def enigmaEncipher(self, letter):
        self.__kb = Keyboard()

        # Rotate the rotors
        self.rotateRotors()

        # ----------FORWARD PASS----------
        # Keyboard
        signal = self.__kb.keyboardForward(letter)
        # Plugboard
        signal = self.__pb.plugboardForward(signal)
        # Rotors
        signal = self.__rotor3.rotorForward(signal)
        signal = self.__rotor2.rotorForward(signal)
        signal = self.__rotor1.rotorForward(signal)

        # Reflector
        signal = self.__reflector.reflect(signal)

        # ----------BACKWARD PASS----------
        # Rotors
        signal = self.__rotor1.rotorBackward(signal)
        signal = self.__rotor2.rotorBackward(signal)
        signal = self.__rotor3.rotorBackward(signal)
        # Plugboard
        signal = self.__pb.plugboardBackward(signal)
        # Keyboard
        letter = self.__kb.keyboardBackward(signal)

        return letter
    
    def rotateRotors(self):
        r3Right = self.__rotor3.getWires()[0]
        r2Right = self.__rotor2.getWires()[0]
        r3Notch = self.__rotor3.getNotch()
        r2Notch = self.__rotor2.getNotch()
    
        # Explanation of Enigma Rotation Mechanism
        # The first rotor rotates one step on every keypress
        # The second rotor normally (double stepping anomaly) rotates whenever the first rotor has completed a full rotation (i.e. the first rotor is in the notch position)
        # The third rotor only rotates when the second rotor has completed a full rotation (i.e. the second rotor is in the notch position)

        # The first wheel rotates one step on every keypress
        self.__rotor3.rotate()

        # The second wheel (normally) rotates on every 26th keypress, whenever the first wheel is in the notch position
        if r3Right[0] == r3Notch:
            self.__rotor2.rotate()

        # The third wheel rotates on every 26th keypress, whenever the second wheel is in the notch position
        if r2Right[0] == r2Notch:
            self.__rotor1.rotate()
    
    def setPlugboard(self, pbList=[]):
        self.__pb = Plugboard(pbList)

    def setRotors(self, r1Type='I', r2Type='II', r3Type='III'):
        self.__rotor1 = Rotor(r1Type)
        self.__rotor2 = Rotor(r2Type)
        self.__rotor3 = Rotor(r3Type)
    
    def setReflector(self, reflectorType='UKW-B'):
        self.__reflector = Reflector(reflectorType)
    
    def setRotorPositions(self, r1Pos, r2Pos, r3Pos):
         # Rotate the rotors to the correct position
        self.__rotor1.rotateToLetter(r1Pos)
        self.__rotor2.rotateToLetter(r2Pos)
        self.__rotor3.rotateToLetter(r3Pos)
    
    def setRingSettings(self, ring1, ring2, ring3):
        # Set the ring settings
        self.__rotor1.setRing(ring1)
        self.__rotor2.setRing(ring2)
        self.__rotor3.setRing(ring3)