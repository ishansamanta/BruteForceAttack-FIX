import time

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
        print ("Ente your username and password")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        def secret_language(password):
            """Encode a message by reversing it and adding secret padding"""
            reversed_msg = password[::-1]
            encoded_msg = "@347648^haj#hag^kol*ihardfhsecu785roamapple" + reversed_msg + "fire94347fiewr53325igreatfhefhifhefhf8helpf3r8hfnapplemohwicsi"
            return encoded_msg

        print(" Attempting to log in...")
        with open("user_encrypted.txt", "r") as file:
            content = file.read().strip()
            encoded_password = secret_language(password)
            if username == self._username and encoded_password == content:
                print(" Login successful! Welcome,", self._username)
                self._failed_attempts = 0  # Reset after success
            if self._locked:
              print(" You can try to log in again")
              return

   
            else:
              self._failed_attempts += 1
              print(" Incorrect username or password.")

            if self._failed_attempts >= 3:
                self._locked = True
                print(" Too many failed attempts. Account locked!")
                print(" Account will be locked for 10 seconds...")
                for i in range(10, 0, -1):  #cooldown added
                    print(i)
                    time.sleep(2) # 2- second wait


login_system = SimpleLogin("ishan", "secure@123")

# Bruteforce Simulation (try attacking with wrong passwords)
login_system.login("ishan", "123")
login_system.login("ishan", "admin")
login_system.login("ishan", "root")  # Locked now

# should be blocked
login_system.login("ishan", "secure@123")    #If u want to change the password change here and also use the encoder file to encode it and update the user_encrypted.txt file with the encoded one

