"""
AUTHOR: Ryan Yeo
STUDENT ID: 2214452
CLASS: DAAA/2B/01
"""

from MainProgramme.MenuOptions import MenuOptions

class CipherCLI(MenuOptions):
    """
    This class handles the user interface of the program.
    It inherits from the MenuOptions class, which contains the methods
    """
    def __init__(self):
        super().__init__()

    def starting_screen(self):
        starting_text="""
*************************************************************************
* ST1507 DSAA: Welcome to:                                              *
*                                                                       *
*     ~ Caesar Cipher Encrypted Message Analyzer ~                      *
*-----------------------------------------------------------------------*
*                                                                       *
*  - Done by: Ryan Yeo (2214452)                                        *
*  - Class DAAA/2B/01                                                   *
*************************************************************************
"""
        print(starting_text)
        
    def continueProgram(self) -> None:
        self.getUserInput("Press Enter key, to continue....", value="")
    

    def getMenuInput(self):
        menu_text = """
Please select your choice: (1,2,3,4,5,6,7,8)
    1. Encrypt/Decrypt Message
    2. Encrypt/Decrypt File
    3. Analyze letter frequency distribution
    4. Infer caesar cipher from file
    5. Analyze and sort encrypted files
    6. Vigenere Cipher (Bonus)
    7. Encrypt/Decrypt text with Enigma Machine (Bonus)
    8. Exit
Enter choice:  """

        menu_input = self.getUserInput(menu_text, "int", [1,8])
        return menu_input

    def run(self):
        self.starting_screen()
        while self.isRunning:
            self.continueProgram()
            menu_input = self.getMenuInput()
            self.options[str(menu_input)]()
