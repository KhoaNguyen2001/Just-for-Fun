from config import Settings
from utils import Helper, GameHandler, StatisticHandler, SettingsHandler

def playGame():
    statistics = StatisticHandler()

    questions = GameHandler.getAllQuestions(Settings.QUESTIONS_PATH)
    question = GameHandler.getOneQuestion(questions)
    GameHandler.displayQuestion(question)

    user_answer = Helper.getUserAnswer(message="Your answer (type the option number): ", valid_options=[1, 2, 3, 4], reset_index=True)
    isTrue = GameHandler.checkAnswer(question, user_answer)

    statistics.updateWithResult(isTrue)
    statistics.setStatistics()

if __name__ == "__main__":
    while True:
        choice = Helper.getMenuChoice()
        if choice == 1:
            while True:
                playGame()
        elif choice == 2:
            statistics = SettingsHandler()
            while True:
                choice = statistics.getMenuChoice()
                if choice == 1:
                    statistics.resetStatistics()
                elif choice == 2:
                    break
        elif choice == 3:
            print("Thank you for playing!")
            break
