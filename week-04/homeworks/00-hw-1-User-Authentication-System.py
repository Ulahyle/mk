import hashlib


class AuthException(Exception):
    pass

class UsernameAlreadyExists(AuthException):
    pass

class PasswordTooShort(AuthException):
    pass

class InvalidUsername(AuthException):
    pass

class InvalidPassword(AuthException):
    pass


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.is_logged_in = False

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    def check_password(self, password):
        return self.password == self.hash_password(password)
    

class Athenticator:
    def __init__(self):
        self.users = {}

    def add_user(self, username, password):
        if username in self.user:
            raise UsernameAlreadyExists("This username is taken")
        if len(password) < 8:
            raise PasswordTooShort("Password must be at least 8 characters.")
        
        self.users[username] = User(username, password)
        print(f"User '{username}' regesterd successfully.")

    def login(self, username, password):
        if username not in self.user:
            raise InvalidUsername("The username doesn't exist!")
        user = self.users[username]
        if not user.check_password(password):
            raise InvalidPassword("The password is incorrect!")
        
        user.is_logged_in = True
        print(f"User '{username}' is logged in")

    def is_logged_in(self, username):
        if username not in self.users:
            raise InvalidUsername("The username doesn't exist!")
        return self.user[username].is_logged_in
        