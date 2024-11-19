from authenticator import Authenticator
from authorizor import Authorizor

# Ajouter un utilisateur
authenticator.add_user("Alice", "password123")

# Ajouter des permissions
authorizor.add_permission("view_reports")
authorizor.add_permission("edit_reports")

# Connecter un utilisateur
authenticator.login("Alice", "password123")

# Accorder des permissions
authorizor.grant_permission("Alice", "view_reports")

# Vérifier les permissions
try:
    authorizor.check_permission("Alice", "edit_reports")
except PermissionError as e:
    print(e)  # User 'Alice' does not have permission 'edit_reports'