"""
AUTHOR: Ryan Yeo
STUDENT ID: 2214452
CLASS: DAAA/2B/01
"""

from Utils.Utils import Utils
from datetime import date
import string

class MenuOptions(Utils):
    """
    This class contains the methods that are used by the CipherCLI class
    Each method is a menu option that the user can choose from
    """
    def __init__(self):
        super().__init__()
        self.options = {
            '1': self.EncryptDecryptMessage,
            '2': self.EncryptDecryptFile,
            '3': self.AnalyzeLetterFrequencyDistribution,
            '4': self.InferCaesarCipherFromFile,
            '5': self.AnalyzeAndSortEncryptedFiles,
            '6': self.VigenereCipher,
            '7': self.EnigmaMachine,
            '8': self.Exit
        }
        self.isRunning = True

    # Option 1
    def EncryptDecryptMessage(self):
        option, text, key = self.getCaesarInput()

        if option == 'E':
            new_text = self.Ciphers.Caesar.caesarCipher(text, key)
        else:
            new_text = self.Ciphers.Caesar.caesarCipher(text, -key)

        self.printCaesarOutput(option, text, new_text, key)
    
    # Option 2
    def EncryptDecryptFile(self):
        option, text, key = self.getCaesarInput(IFile=True)

        if option == 'E':
            new_text = self.Ciphers.Caesar.caesarCipher(text, key)
        else:
            new_text = self.Ciphers.Caesar.caesarCipher(text, -key)

        self.printCaesarOutput(option, text, new_text, key, OFile=True)
        
    # Option 3
    def AnalyzeLetterFrequencyDistribution(self):
        
        text = self.getUserInput("Please enter the file you want to analyze: ", "file", mode='r')
        print('\n')

        self.LetterAnalysis.analyseFreq(text)
        plot = []
        lettersList = self.LetterAnalysis.getCounter().counterToList("letter")
        percentageList = self.LetterAnalysis.getCounter().counterToList("percentage")
        
        # Padding by building Empty Column
        plot.append(self.LetterAnalysis.buildColumn(None))

        for letter in string.ascii_uppercase:
            index = lettersList.index(letter)
            plot.append(self.buildColumn(letter, percentageList[index]))
            # Padding by building Empty Column
            plot.append(self.buildColumn(None))
        
        # Reformat Plot
        plot = self.reformatPlot(plot)

        # Add the numerical statistics
        plot = self.numericalStatistics(plot, lettersList, percentageList)

        # Finally join it into string
        plot = "\n".join(plot)

        print(plot)

        # Choice to export the findings to a .txt file
        export = self.getUserInput("\nDo you want to export the findings to a .txt file? (Y/N): ", "categorical", category=['Y', 'N'])
        if export == 'Y':
            exportFile = self.getUserInput("Please enter the file you want to export to: ", "file", mode='w')
            self.exportFindings(exportFile)
        
    # Option 4
    def InferCaesarCipherFromFile(self):
        text = self.getUserInput("Please enter the file to analyse: ", "file", mode='r')
    
        masterText = self.getUserInput("Please enter the reference frequencies file: ", "refFile")
        masterText = masterText.split('\n')

        masterFreq = {line.split(',')[0].upper() : float(line.split(',')[1]) for line in masterText}

        bestShift = self.Ciphers.Caesar.caesarBestShift(text, masterFreq)

        print(f"The inferred caesar cipher key is: {bestShift}")
        export = self.getUserInput("Would you want to decrypt this file using this key? y/n: ", "categorical", category=['Y', 'N'])

        if export == 'Y':
            new_text = self.caesarCipher(text, -bestShift)
            self.printCaesarOutput('D', text, new_text, bestShift, OFile=True)

    # Option 5
    def AnalyzeAndSortEncryptedFiles(self):
        # Clear sorted list
        self.clearSortText()

        dir, files = self.getUserInput("Please enter the folder name: ", "folder")
        
        masterText = self.getUserInput("Please enter the reference frequencies file: ", "refFile")
        masterText = masterText.split('\n')

        masterFreq = {line.split(',')[0].upper() : float(line.split(',')[1]) for line in masterText}

        for file in files:
            with open(f"{dir}/{file}", 'r') as f:
                if file == 'log.txt':
                    continue
                text = f.read()
                shift = self.Ciphers.Caesar.caesarBestShift(text, masterFreq)
                self.addTextfile(file, shift, text)
        
        # Convert to list
        sortedFiles = self.getTextfiles().textfileToList("filename")
        sortedShifts = self.getTextfiles().textfileToList("shift")
        sortedTexts = self.getTextfiles().textfileToList("text")

        log = []

        for i, (file, shift) in enumerate(zip(sortedFiles, sortedShifts)):
            msg = f"Decrypting: {file} with key: {shift} as file: file{i+1}.txt"
            print(msg + '\n')
            log.append(msg)
        
        # Write back into dir
        for i, (text, shift) in enumerate(zip(sortedTexts, sortedShifts)):
            with open(f"{dir}/file{i+1}.txt", 'w') as f:
                f.write(self.Ciphers.Caesar.caesarCipher(text, -shift))

        # If log file already exists, append to it
        if 'log.txt' in files:
            with open(f"{dir}/log.txt", 'a') as f:
                # Add a divider
                f.write('\n' + '-'*100 + '\n')
                # Add current date
                today = date.today()
                f.write(today.strftime("%B %d, %Y"))
                f.write('\n' + '-'*100 + '\n')
                f.write("\n".join(log))

        # Write to log file
        else:
            with open(f"{dir}/log.txt", 'w') as f:
                f.write("\n".join(log))

                

    # Option 6
    def VigenereCipher(self):
        option, text, key = self.getVigenereInput()

        if option == 'E':
            print(self.Ciphers.Vigenere.vigenereCipher(text, key, encrypt=True))
        else:
            print(self.Ciphers.Vigenere.vigenereCipher(text, key, encrypt=False))
    
    # Option 7
    def EnigmaMachine(self):
        info = self.getUserInput("Would you like to learn more about the Enigma Machine? (Y/N): ", "categorical", category=['Y', 'N'])
        if info == 'Y':
            print("""
The Enigma Machine is a cipher machine that can be used to both encrypt and decrypt messages.
It was used by the Nazi Germany during World War 2 to encrypt their messages from the allied forces but it was eventually decrtypted by Alan Mathison Turing.

Before using the Enigma Machine, there are several settings that must be set:
    1. Plubgbard Settings: The plugboard is used to switch two letters encryption 
    e.g. A is encrypted to F and R is encrypted to B, then using a plugboard connnecting A-R would result in A being encrypted to B and R being encrypted to F
                  
    2. Rotors: Typically there are 3 rotors in the Enigma Machine (though the Navy used 4), each rotor has 26 different settings, each setting is a permutation of the 26 letters in the alphabet. 
    Each rotor is used to scramble the letters once before being encrypted. Each time a key is pressed, one of the rotor turns and thus the encryption for the same letter changes
                  
    3. Reflector: The reflector is used to reflect the signal back to the rotors after it has been encrypted by the rotors. The reflector is used to ensure that the encryption is reversible. It is similar to a Rotor but it does not turn.
                  
    4. Starting Position of Rotor: The starting position of the rotor is used to determine which permutation of the rotor is used to encrypt the letter.
                  
    5. Ring Settings: The ring settings are used to set the starting position of the rotors. In an enigma machine, there are three rotors and thus three ring settings. 

To learn more about the Enigma Machine, please visit: https://youtube.com/watch?v=ybkkiGtJmkM
Or play around with the following Enigma Machine Simulator: 
    - https://cryptii.com/pipes/enigma-machine
    - https://mckoss.com/enigma-simulator-js/

Note: Our implementation of the Enigma Machine is a model I Enigma Machine, which means that:
    -  The reflector options are limited to UKW-A, UKW-B and UKW-C
    - The rotor options are limited to I, II, III, IV and V

The implementation is also not entirely accurate as we have chosen to preserve spaces which was not the case in the actual Enigma Machine.
""")
            
        text = self.getUserInput("Please enter the text you want to encrypt/decrypt: ", "str")

        rotor1 = self.getUserInput("Please enter the first rotor (I, II, III, IV, V): ", "categorical", category=['I', 'II', 'III', 'IV', 'V'])
        r1Pos = self.getUserInput("Please enter the starting position of the first rotor (A-Z): ", "categorical", category=string.ascii_uppercase)
        r1Ring = self.getUserInput("Please enter the ring setting of the first rotor (1-26): ", "int", [1,26])

        rotor2 = self.getUserInput("Please enter the second rotor (I, II, III, IV, V): ", "categorical", category=['I', 'II', 'III', 'IV', 'V'])
        r2Pos = self.getUserInput("Please enter the starting position of the second rotor (A-Z): ", "categorical", category=string.ascii_uppercase)
        r2Ring = self.getUserInput("Please enter the ring setting of the second rotor (1-26): ", "int", [1,26])

        rotor3 = self.getUserInput("Please enter the third rotor (I, II, III, IV, V): ", "categorical", category=['I', 'II', 'III', 'IV', 'V'])
        r3Pos = self.getUserInput("Please enter the starting position of the third rotor (A-Z): ", "categorical", category=string.ascii_uppercase)
        r3Ring = self.getUserInput("Please enter the ring setting of the third rotor (1-26): ", "int", [1,26])

        reflector = self.getUserInput("Please enter the reflector (UKW-A, UKW-B, UKW-C): ", "categorical", category=['UKW-A', 'UKW-B', 'UKW-C'])

        plugboard = self.getUserInput("Please enter the plugboard settings (e.g. AB CD EF): ", "plugboard")   

        self.Ciphers.Enigma.setPlugboard(plugboard)
        self.Ciphers.Enigma.setRotors(rotor1, rotor2, rotor3)
        self.Ciphers.Enigma.setReflector(reflector)
        self.Ciphers.Enigma.setRotorPositions(r1Pos, r2Pos, r3Pos)
        self.Ciphers.Enigma.setRingSettings(r1Ring, r2Ring, r3Ring) 

        new_text = ""
        for letter in text:
            # If its an alphabet
            if letter.upper() in string.ascii_uppercase:
                new_text += self.Ciphers.Enigma.enigmaEncipher(letter)
            # If its a space
            elif letter == ' ':
                new_text += letter
            # Ignore all other characters

        print(f"Input: \t\t{text}")
        print(f"Output:\t\t{new_text}")

    
    # Option 8
    def Exit(self):
        self.isRunning = False
        print("\nBye, thanks for using ST1507 DSAA: Caesar Cipher Encrypted Message Analyzer")
    