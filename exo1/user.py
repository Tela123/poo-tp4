import hashlib

class User:
    def __init__(self, username, password):
        self.username=username
        self.password=password
        self.statuts=False
        
    def check_password(self, password)->bool:
        encrypted_password=self._encrypt_password(password)
        return self.password==password
    
    def _encrypt_password(self, password)->str:
        '''
            cette methode per;et de crypter
        '''
        password_encoded=password.encode('utf-8')
        return hashlib.sha256(password_encoded).hexdigest()
user=User('telah', 'tela')
print(user.check_password('tela4'))
# print(user._encrypt_password())