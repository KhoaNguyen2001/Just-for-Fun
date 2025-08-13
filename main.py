from config import Settings
from utils import GameHandler, StatisticHandler

def playGame():
    statistics = StatisticHandler()

    questions = GameHandler.getAllQuestions(Settings.QUESTIONS_PATH)
    question = GameHandler.getOneQuestion(questions)
    GameHandler.displayQuestion(question)

    user_answer = GameHandler.getUserAnswer(message="Your answer (type the option number): ", valid_options=[1, 2, 3, 4])
    isTrue = GameHandler.checkAnswer(question, user_answer)

    statistics.updateWithResult(isTrue)
    statistics.setStatistics()

if __name__ == "__main__":
    while True:
        playGame()
