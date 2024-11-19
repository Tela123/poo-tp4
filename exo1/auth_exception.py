class AuthException(Exception):
    '''
        gere les exceptions:possibles erreurs
    '''
    def __init__(self, username,user):
        super().__init__(self, username, user=None)
        self.username=username
        self.user=user
      
class UserNotFound(AuthException):
    """Utilisateur non trouvé."""
    pass
  
class UsernameAlreadyExists(AuthException):
    pass
class PasswordTooShort(AuthException):
    pass
class InvalidUsername(AuthException):
    pass
class InvalidPassword(AuthException):
    pass
class NopPermission(AuthException):
    pass