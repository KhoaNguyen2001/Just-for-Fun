import os
from utils.FileHandler import FileHandler

class GameHandler:
    @staticmethod
    def getAllQuestions(questions_folder_path: str) -> list:
        questions = []
        for filename in os.listdir(questions_folder_path):
            if filename.endswith('.json'):
                file_path = os.path.join(questions_folder_path, filename)
                question_data = FileHandler.readJsonFile(file_path)
                questions.append(question_data)
        
        return questions
