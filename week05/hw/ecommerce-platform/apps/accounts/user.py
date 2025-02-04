# import json
# import os


# json_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "database", "data", "json")
# file_path = os.path.join(json_folder, "user_data.json")


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

# #updated code to use json instead of txt
# class UserManager:
#     def __init__(self):
#         json_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "database", "data", "json")
#         file_path = os.path.join(json_folder, "user_data.json")
#         self.file_path = file_path
    
#     def read_users(self):
#         try:
#             with open(self.file_path, "r") as file:
#                 return json.load(file)
#         except (FileNotFoundError, json.JSONDecodeError):
#             return[]
        
#     def signin(self, user):
#         users = self.read_users()
#         print(type(users))
#         for signed_user in users:
#             if signed_user['username'] == user.username:
#                 print("error: Username already exist!")
#                 return False
#         users.append({'username': user.username, 'password': user.password})
#         with open(file_path, "a") as file:
#             json.dump(users, file)
#         print(f"User '{user.username}' saved successfully!")
#         return True
    
#     def login(self, username, password):
#         users = self.read_users()
#         print(users)
#         for signed_user in users:
#             if signed_user['username'] == username and signed_user['password'] == password:
#                 print(f"welcome back {username}! (:")
#                 return True
#         print("incorrect username or password")
#         return False
    

import os

txt_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "database", "data", "txt")
file_path = os.path.join(txt_folder, "user_data.txt")

class UserManager:
    def __init__(self, file_path):
     self.file_path = file_path

    def read_users(self):
        try:
            with open(file_path, "r") as file:
                return [line.strip() for line in file.readlines()] 
        except FileNotFoundError:
            return[]

    def signin(self, user):
        users = self.read_users()
        for signed_user in users:
            saved_username, _ = signed_user.split(",")
            if saved_username == user.username:
                print("error: Username already exist!")
                return False
            
        with open(file_path, "a") as file:
            file.write(f"{user.username}, {user.password}\n")
        print(f"User '{user.username}' saved successfully!")
        return True

    def login(self, username, password):
        users = self.read_users()
        for signed_user in users:
            saved_username, saved_password = signed_user.split(", ")
            if saved_username == username and saved_password == password:
                print(f"welcome back {username} (:")
                return True
            print("incorrect username or password")
            return False