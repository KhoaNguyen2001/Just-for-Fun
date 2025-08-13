from config import Settings
from .FileHandler import FileHandler

class StatisticHandler:
    def __init__(self):
        self.__statistics = FileHandler.readJsonFile(Settings.STATISTICS_PATH)

    def getStatistics(self) -> dict:
        return self.__statistics
    
    def setStatistics(self) -> None:
        FileHandler.writeJsonFile(Settings.STATISTICS_PATH, self.__statistics)

    def updateWithResult(self, isTrue: bool) -> None:
        if isTrue:
            self.__statistics["correct_answers"] += 1
        else:
            self.__statistics["incorrect_answers"] += 1