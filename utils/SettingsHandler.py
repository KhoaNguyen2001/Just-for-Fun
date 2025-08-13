from config import Settings
from .IOHandler import IOHandler
from .FileHandler import FileHandler
from .Helper import Helper

STATISTICS_PATH = Settings.STATISTICS_PATH

class SettingsHandler:
    def __init__(self):
        self.__statistics = FileHandler.readJsonFile(STATISTICS_PATH)

    @staticmethod
    def getMenuChoice() -> int:
        print("Select an option:")
        print("    1. Reset Statistics")
        print("    2. Quit")
        return Helper.getUserAnswer(message="Enter your choice (1-2): ", valid_options=[1, 2], reset_index=False)

    def resetStatistics(self):
        self.__statistics = {
            "correct_answers": 0,
            "incorrect_answers": 0
        }
        FileHandler.writeJsonFile(STATISTICS_PATH, self.__statistics)
        IOHandler.printSuccess("Statistics have been reset successfully!")