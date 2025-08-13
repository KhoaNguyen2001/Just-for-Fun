from config import Settings
from utils import GameHandler

if __name__ == "__main__":
    questions = GameHandler.getAllQuestions(Settings.QUESTIONS_PATH)
    print(questions)