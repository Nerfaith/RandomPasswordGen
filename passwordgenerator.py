import random
import string

# Get the random password
def get_random_password_string(length):
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(password_characters) for i in range(length))
    print("Random string password is:", password)

get_random_password_string(10)
get_random_password_string(10)