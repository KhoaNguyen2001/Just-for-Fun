from .IOHandler import IOHandler

class Helper:
    @staticmethod
    def getUserAnswer(message: str, valid_options: list, reset_index: bool = False) -> str:
        input_value = input(message)
        if input_value.isdigit() and int(input_value) in valid_options:
            return int(input_value) - int(reset_index)
        else:
            IOHandler.printError(f"Invalid input! Please enter a number in {{{','.join(map(str, valid_options))}}}")
            return Helper.getUserAnswer(message, valid_options)
        
    @staticmethod
    def getMenuChoice() -> int:
        print("Select an option:")
        print("    1. Start Game")
        print("    2. View Statistics")
        print("    3. Quit")
        return Helper.getUserAnswer(message="Enter your choice (1-3): ", valid_options=[1, 2, 3], reset_index=False)