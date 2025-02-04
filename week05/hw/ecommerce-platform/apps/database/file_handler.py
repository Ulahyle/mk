import os

txt_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "txt")
file_path = os.path.join(txt_folder, "user_data.txt")


def save_user_data(user_name, user_email):
    try:
        with open(file_path, "a") as file:
            file.write(f"{user_name}, {user_email}\n")
        print(f"User '{user_name}' saved successfully!")
    except Exception as e:
        print(f"an Unexpected error occurred: {e}")


def read_user_data():
    try:
        with open(file_path, "r") as file:
            content = file.readlines()
            if not content:
                print("no data")
            else:
                print("User data: ")
                for line in content:
                    print(line.strip())
    except FileNotFoundError:
        print("Error: the file 'user_data.txt' does not exist. create it first")
    except Exception as e:
        print(f"an Unexpected error occurred: {e}")

    

save_user_data("ula", 00)
read_user_data()