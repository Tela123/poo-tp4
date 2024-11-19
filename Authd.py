from user import User
from exceptions import UserNotFound, InvalidPassword

class Authenticator:
    """Gère l'enregistrement, la connexion et la déconnexion des utilisateurs."""
    def __init__(self):
        self.users = {}  # Stockage des utilisateurs
        self.logged_in_users = {}  # Utilisateurs connectés

    def add_user(self, username, password):
        if username in self.users:
            raise ValueError(f"User '{username}' already exists.")
        self.users[username] = User(username, password)

    def login(self, username, password):
        if username not in self.users:
            raise UserNotFound(username)
        user = self.users[username]
        if not user.check_password(password):
            raise InvalidPassword(username)
        self.logged_in_users[username] = user

    def logout(self, username):
        if username in self.logged_in_users:
            del self.logged_in_users[username]