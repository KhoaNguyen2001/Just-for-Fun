from enums import Color

class IOHandler:
    @staticmethod
    def printWithColor(text: str, color: Color = Color.RESET) -> None:
        colored_text = f"{color.value}{text}{Color.RESET.value}"
        print(colored_text)

    @staticmethod
    def printError(text: str) -> None:
        IOHandler.printWithColor(text, Color.RED)

    @staticmethod
    def printSuccess(text: str) -> None:
        IOHandler.printWithColor(text, Color.GREEN)

    @staticmethod
    def printInfo(text: str) -> None:
        IOHandler.printWithColor(text, Color.BLUE)

    @staticmethod
    def printDebug(text: str) -> None:
        IOHandler.printWithColor(text, Color.RESET)

    @staticmethod
    def printWarning(text: str) -> None:
        IOHandler.printWithColor(text, Color.YELLOW)

    @staticmethod
    def printCritical(text: str) -> None:
        IOHandler.printWithColor(text, Color.MAGENTA)

    @staticmethod
    def printAlert(text: str) -> None:
        IOHandler.printWithColor(text, Color.CYAN)
