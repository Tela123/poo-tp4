import hashlib

class User:
    """Représente un utilisateur avec un nom d'utilisateur et un mot de passe crypté."""
    def __init__(self, username, password):
        self.username = username
        self.password_hash = self._encrypt_password(password)

    def _encrypt_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password):
        return self.password_hash == self._encrypt_password(password)