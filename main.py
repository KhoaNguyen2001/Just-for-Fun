from config import Settings
from utils import GameHandler, IOHandler

if __name__ == "__main__":
    questions = GameHandler.getAllQuestions(Settings.QUESTIONS_PATH)
    IOHandler.printInfo(questions)
    print('Hello')