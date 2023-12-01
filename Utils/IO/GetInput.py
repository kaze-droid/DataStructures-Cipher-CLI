"""
AUTHOR: Ryan Yeo
STUDENT ID: 2214452
CLASS: DAAA/2B/01
"""

import os

class GetInput:
    # Improved input function with type checking
    def getUserInput(self, question: str, type: str  = "str", range: ("list[float] | None") = None, category: ("list[str] | None") = None, value: ("str | None") = None, mode: str = 'r') -> "int | str | float":
        """
        Gets the user input with type checking

        Parameters
        ----------
        question : str
            The question to be asked with getInput()
        type : str, optional
            The type of input used for type checking, by default "str" 
        range : (list[float] | None), optional
            The range of input to be accepted if type is float or int, by default None
        category : (list[str] | None), optional
            The list of categories to be accepted if type is categorical, by default None
        value : (str | None), optional
            The value to be accepted if type is str, by default None
        mode : str, optional
            The mode to be used if type is file, by default 'r'
        """
        
        if type not in ['str', 'strictStr', 'categorical', 'int', 'float', 'bool', 'file', 'refFile', 'folder', 'plugboard']:
            raise ValueError(f"Type must be one of the following: 'str', 'strictStr', 'categorical', 'int', 'float', 'bool', 'file', 'refFile', 'folder', 'plugboard but received {type}")

        success = False

        while not success:
            print('\n')
            reply = input(question)

            # Specified int input
            if type == 'int':
                try:
                    reply = int(reply)
                    if range is not None and (reply < range[0] or reply > range[1]):
                        print(f"\nInput must be a number between {range[0]}-{range[1]}")
                    else:
                        success = True
                except ValueError:
                    print("\nInput must be a number")
            
            # Specified string input
            elif type == 'str':
                if value is None or reply == value:
                    success = True

            # Specified float input
            elif type == 'float':
                try:
                    reply = float(reply)
                    if range is not None and (reply < range[0] or reply > range[1]):
                        print(f"\nInput must be a number between {range[0]}-{range[1]}")
                    else:
                        success = True
                except ValueError:
                    print("\nInput must be a float")
        
            # Specified boolean input
            elif type == 'bool':
                if reply.lower() not in ['y', 'n', 'yes', 'no']:
                    print("\nInput must be 'y' or 'n'")
                else:
                    success = True
                    reply = 'y' if reply.lower() in ['y', 'yes'] else 'n'
            
            # Specified categorical input
            elif type == 'categorical':
                # Check upper case
                if reply.upper() not in category:
                    print(f"\nInput must be one of the following: {', '.join(category)}")
                else:
                    success = True
                    reply = reply.upper()
            
            # Specified file input with read mode
            elif type == 'file':
                try:
                    with open(reply, 'r') as f:
                        if mode == 'r':
                            reply = f.read()
                            if reply == "":
                                print("File should not be empty!\n")
                            else:
                                success = True
                        elif mode == 'w':
                            overwrite = self.getUserInput("\nThis file already exists! Do you want to overwrite it? (y/n): ", "bool")
                            if overwrite == 'y':
                                success = True

                # File does not exist
                except FileNotFoundError:
                    # Cannot read file that does not exist
                    if mode == 'r':
                        print("\nThis file does not exist!")
                    # Write to new file
                    elif mode == 'w':
                        # Check if file extension is .txt
                        if reply[-4:] != '.txt':
                            print("\nFile must be a .txt file")
                        else:
                            success = True

                # Error opening file
                except Exception as e:
                    print(f"\nError: {e}")
                
            # Specified a reference file
            elif type == 'refFile':
                try:
                    with open(reply, 'r') as f:
                        seen_letters = set()
                        reply = f.read()
                        validated = True
                        validation_msg = ""

                        # Validate the reference file is in the right format
                        for line in reply.split('\n'):
                            parts = line.strip().split(',')
                            # Check if the line has exactly 2 parts
                            if len(parts) != 2:
                                validated = False
                                validation_msg = "Error: Missing Comma"
                                break
                            
                            # Check if the first part is a letter and that it is not seen before
                            if not parts[0].isalpha() or len(parts[0]) != 1:
                                validated = False
                                validation_msg = "Error: First part is not a letter"
                                break
                            
                            # Check if the second part is a float
                            try:
                                float(parts[1])
                                if float(parts[1]) <= 0 or float(parts[1]) > 100:
                                    validated = False
                                    validation_msg = "Error: Second part is not a float between (0, 100]"
                            except ValueError:
                                validated = False
                                validation_msg = "Error: Second part is not a float"
                            
                            # Check if the letter is not seen before
                            if parts[0].upper() in seen_letters:
                                validated = False
                                validation_msg = "Error: Letter is seen before"
                            else:
                                seen_letters.add(parts[0].upper())

                        if validated:
                            if len(seen_letters) != 26:
                                validated = False
                                validation_msg = "Error: Reference file does not contain all 26 letters of the alphabet"

                            else:
                                success = True

                        if not success:
                            print(f"\n{validation_msg}")
                            print("Reference file is must in the format <letter>,<freq> for each line and must contain all 26 letters of the alphabet with freq being between (0, 100]")

                # File does not exist
                except FileNotFoundError:
                    # Cannot read file that does not exist
                    if mode == 'r':
                        print("\nThis file does not exist!")

            # Specified a folder
            elif type == 'folder':
                if os.path.isdir(reply):
                    success = True
                    # Return all the files in the folder
                    dirs = os.listdir(reply)
                    # Only extract the .txt files
                    reply = (reply, [file for file in dirs if file[-4:] == '.txt' and not file.startswith('file')])
                else:
                    print("\nThis folder does not exist!")
            
            # Specified a plugboard
            elif type == 'plugboard':
                # Empty Plugboard
                if reply == '':
                    pairs = []
                    success = True
                else:
                    pairs = reply.split(' ')
                    # Check that each pair in pairs is valid
                    seen_letters = set()
                    validated = True
                    for pair in pairs:
                        # Check if the pair is valid
                        if len(pair) != 2:
                            validated = False
                            break
                        # Check if the pair is valid
                        if pair[0].isalpha() and pair[1].isalpha():
                            # Check if the pair is not seen before
                            if pair[0].upper() in seen_letters or pair[1].upper() in seen_letters:
                                validated = False
                                break
                            else:
                                seen_letters.add(pair[0].upper())
                                seen_letters.add(pair[1].upper())
                        else:
                            validated = False
                            break
                    
                    if validated:
                        success = True
                        reply = pairs
                    
                    else:
                        print("\nPlugboard must be in the format <letter><letter> with each pair separated by a space")
                        print("Each letter can only be used once")
                        print("Plugboard can be left empty")

            elif type == 'strictStr':
                if reply.isalpha():
                    success = True
                else:
                    print("\nInput must be a string")
        
        return reply
    
    def getCaesarInput(self, IFile: bool=False) -> (str, str, int):
        """
        Gets the input for the caesar cipher

        Parameters
        ----------
        IFile : bool, optional
            Whether the input is from a file, by default False

        Returns
        -------
        option : str
            'E' for encrypt, 'D' for decrypt
        text : str
            The text to be encrypted/decrypted
        key : int
            The key to be used for encryption/decryption
        """

        option = self.getUserInput('Enter "E" for Encrypt or "D" for Decrypt: ', "categorical", category=['E', 'D'])
        if IFile==False:
            text = self.getUserInput(f"Please type text you want to {'encrypt' if option == 'E' else 'decrypt'}: ")
        else:
            text = self.getUserInput(f"Please enter the file you want to {'encrypt' if option == 'E' else 'decrypt'}: ", "file", mode='r')
        key = self.getUserInput("Enter the cipher key: ", "int", range=[-26, 26])
        return option, text, key

    def getVigenereInput(self) -> (str, str, str):
        option = self.getUserInput('Enter "E" for Encrypt or "D" for Decrypt: ', "categorical", category=['E', 'D'])
        text = self.getUserInput(f"Please type text you want to {'encrypt' if option == 'E' else 'decrypt'}: ")
        key = self.getUserInput("Enter the cipher key: ", "strictStr")

        return option, text, key