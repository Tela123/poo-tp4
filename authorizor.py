class Authorizor:
    """Gère les permissions pour les utilisateurs connectés."""
    def __init__(self, authenticator):
        self.authenticator = authenticator
        self.permissions = {}  # Dictionnaire de permissions

    def add_permission(self, permission):
        if permission in self.permissions:
            raise ValueError(f"Permission '{permission}' already exists.")
        self.permissions[permission] = set()

    def grant_permission(self, username, permission):
        if permission not in self.permissions:
            raise ValueError(f"Permission '{permission}' does not exist.")
        if username not in self.authenticator.users:
            raise UserNotFound(username)
        self.permissions[permission].add(username)

    def check_permission(self, username, permission):
        if username not in self.authenticator.logged_in_users:
            raise NotLoggedIn(username)
        if permission not in self.permissions or username not in self.permissions[permission]:
            raise PermissionError(username, permission)