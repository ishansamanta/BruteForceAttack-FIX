#THIS IS THE WEAK TESTING CODE ,,, TRY RUNNING IT IN YOUR IDE
class SimpleLogin:
    def __init__(self, username, password):
        self._username = username
        self._password = password
        self._failed_attempts = 0
        self._locked = False

    @property
    def is_locked(self):
        return self._locked

    def login(self, username, password):
        if self._locked:
            print(" Account is locked. Too many failed attempts.")
            return

        if username == self._username and password == self._password:
            print(" Login successful! Welcome,", self._username)
            self._failed_attempts = 0  # Reset after success
        else:
            self._failed_attempts += 1
            print(" Incorrect username or password.")

            if self._failed_attempts >= 3:
                self._locked = True
                print(" Too many failed attempts. Account locked!")


login_system = SimpleLogin("ishan", "secure@123")

# Bruteforce Simulation (try attacking with wrong passwords)
login_system.login("ishan", "123")
login_system.login("ishan", "admin")
login_system.login("ishan", "root")  # Locked now

# Try real password (should be blocked)
login_system.login("ishan", "secure@123")
