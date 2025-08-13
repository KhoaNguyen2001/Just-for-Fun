from config import Settings
from .FileHandler import FileHandler

STATISTICS_PATH = Settings.STATISTICS_PATH

class SettingsHandler:
    def __init__(self):
        self.__statistics = FileHandler.readJsonFile(STATISTICS_PATH)

    def clearStatistics(self):
        self.__statistics = {
            "correct_answers": 0,
            "incorrect_answers": 0
        }
        FileHandler.writeJsonFile(STATISTICS_PATH, self.__statistics)