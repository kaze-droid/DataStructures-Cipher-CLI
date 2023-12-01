"""
AUTHOR: Ryan Yeo
STUDENT ID: 2214452
CLASS: DAAA/2B/01
"""

from Utils.IO.DisplayOuput import DisplayOutput
from Utils.IO.GetInput import GetInput

from Utils.Ciphers.Ciphers import Ciphers

from Utils.LetterAnalysis import LetterAnalysis
from Utils.SortText import SortText

# Store all the Utils classes in one class
class Utils(DisplayOutput, GetInput, LetterAnalysis, SortText, Ciphers):
    def __init__(self):
        self.DisplayOutput = DisplayOutput()
        self.GetInput = GetInput()
        self.LetterAnalysis = LetterAnalysis()
        self.SortText = SortText()
        self.Ciphers = Ciphers()
    
                    