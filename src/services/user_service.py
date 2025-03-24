from src.persistence.db_handler import DBHandler

class UserService:
    @staticmethod
    def register(username):
        if DBHandler.add_user(username):
            return "Success"
        return "Error - user already existing"
