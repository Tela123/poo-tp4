class AuthException(Exception):
    """Exception de base pour les erreurs d'authentification."""
    def __init__(self, username, user=None):
        super().__init__(f"Authentication error for user: {username}")
        self.username = username
        self.user = user


class UserNotFound(AuthException):
    """Utilisateur non trouvé."""
    pass


class InvalidPassword(AuthException):
    """Mot de passe invalide."""
    pass


class NotLoggedIn(AuthException):
    """Utilisateur non connecté."""
    pass


class PermissionError(Exception):
    """L'utilisateur n'a pas les permissions nécessaires."""
    def __init__(self, username, permission):
        super().__init__(f"User '{username}' does not have permission '{permission}'")
        self.username = username
        self.permission = permission