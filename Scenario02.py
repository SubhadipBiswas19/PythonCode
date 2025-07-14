"""
You need to design a user registration and login system.
Tasks:
Define a User class with private variables for username and password.
Implement methods to register users and authenticate login attempts. Use encapsulation to protect password data.
Use default and keyword arguments for registration function (e.g., email optional).
Use a dictionary to store users with username as the key.
Implement exception handling for duplicate usernames and wrong password attempts.
Use string formatting (both f-string and .format()) for output messages.
Write a loop that allows multiple login attempts with break and continue controls.
Preconditions:
Username: unique, non-empty string
Password: non-empty string
Email: optional string containing '@' if provided
Login attempts limited to max 3 per session
"""

class User:
    def __init__(self, username, password, email=None):
        self.username = username
        self.password = password
        self.email = email

    def get_username(self):
        return self.username

    def check_password(self, password):
        return self.password == password

    def __str__(self):
        return f"Username: {self.username}, Email: {self.email or 'Not provided'}"

class Login:
    def __init__(self):
        self.users = {}

    def register(self, username, password, email=None):
        try:
            if not username or not password:
                raise ValueError("Username and password cannot be empty.")
            if email and '@' not in email:
                raise ValueError("Invalid email format.")
            if username in self.users:
                raise KeyError("Username already registered.")

            self.users[username] = User(username, password, email)
            print(f"Registration successful for user '{username}'.")

        except ValueError as ve:
            print(f"Registration failed for user '{username}'.")
            print(ve)

        except KeyError as ke:
            print(f"Registration failed for user '{username}'.")
            print(ke)


    def login(self, username):
        attempt = 0
        max_attempts = 3

        if username not in self.users:
            print(f"Username '{username}' not found.\n")
            return

        while attempt < max_attempts:
            password = input(f"Enter Password for '{username}':")
            user = self.users[username]
            if user.check_password(password):
                print(f"Login successful for '{username}'")
                break
            else:
                attempt += 1
                print(f"Wrong password. Attempt {attempt}/{max_attempts}.")
                if attempt < max_attempts:
                    continue
                else:
                    print(f"Max login attempts reached. Access denied.\n")
                    break
if __name__ == "__main__":
    system = Login()

    print("\n--- User Registration ---")
    system.register(username='Subhadip', password='pass123', email='subhadip@mail.com')
    system.register(username='Subham', password='', email='subham@email.com')
    system.register(username='', password='pass123', email='user@email.com')
    system.register(username='aarav', password='pass123', email='aaravemail.com')
    system.register(username='Subhadip', password='pass123', email='subhadip@mail.com')

    print("\n--- Login Session ---")
    system.login("Subhadip")