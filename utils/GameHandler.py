import os
import random
from utils.FileHandler import FileHandler
from utils.IOHandler import IOHandler

class GameHandler:
    @staticmethod
    def getAllQuestions(questions_folder_path: str) -> list:
        questions = []
        for filename in os.listdir(questions_folder_path):
            if filename.endswith('.json'):
                file_path = os.path.join(questions_folder_path, filename)
                question_data = FileHandler.readJsonFile(file_path)
                questions.extend(question_data)
        return questions

    @staticmethod
    def getOneQuestion(questions: list) -> dict:
        if questions:
            return random.choice(questions)
        return {}
    
    @staticmethod
    def displayQuestion(question: dict) -> None:
        if question:
            print(f"Question: {question.get('question', 'No question available')}")
            print("Options:")
            for index, option in enumerate(question.get('options', [])):
                print(f"    {index + 1}. {option}")
        else:
            print("No question to display.")

    @staticmethod
    def checkAnswer(question: dict, user_answer: int) -> bool:
        correct_answer = question.get('answer', '')
        user_answer = question.get('options', [])[user_answer]
        isTrue = user_answer == correct_answer
        IOHandler.printSuccess("Correct!") if isTrue else IOHandler.printError("Incorrect!")
        return isTrue
