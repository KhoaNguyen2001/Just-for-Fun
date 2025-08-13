from config import Settings
from utils import GameHandler, StatisticHandler

if __name__ == "__main__":
    statistics = StatisticHandler()

    questions = GameHandler.getAllQuestions(Settings.QUESTIONS_PATH)

    question = GameHandler.getOneQuestion(questions)
    
    GameHandler.displayQuestion(question)

    user_answer = GameHandler.getUserAnswer("Your answer (type the option number): ")

    isTrue = GameHandler.checkAnswer(question, user_answer)

    statistics = StatisticHandler()

    statistics.updateWithResult(isTrue)

    statistics.setStatistics()
