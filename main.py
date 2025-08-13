from config import Settings
from utils import GameHandler

if __name__ == "__main__":
    questions = GameHandler.getAllQuestions(Settings.QUESTIONS_PATH)

    question = GameHandler.getOneQuestion(questions)
    
    GameHandler.displayQuestion(question)

    user_answer = GameHandler.getUserAnswer("Your answer (type the option number): ")

    