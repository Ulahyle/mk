from apps.accounts.user import User, UserManager

file_path = "database/data/txt/user_data.txt"
# file_path = "database/data/json/user_data.json"

user_manager = UserManager(file_path)

user0 = User("o", "password0")
user_manager.signin(user0)

user1 = User("one", "password1")
user_manager.signin(user1)

user2 = User("one", "password2")
user_manager.signin(user2)

user_manager.login("o", "password0")
user_manager.login("one", "false_password")