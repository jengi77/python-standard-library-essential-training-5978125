# Create a temporary password using Python
import secrets
import string
import random


# Function to return a temporary password given a length
def generate_temp_pass(num_chars=8):
    potential_chars = string.ascii_letters + string.digits + "+=?/!@#$%*"
    result = ''.join(secrets.choice(potential_chars) for i in range(num_chars))
    return result


# Function to return a temporary password and enforce 1 number and 1 uppercase
def generate_better_pass(num_chars=8):
    potential_chars = string.ascii_letters + string.digits + "+=?/!@#$%*"

    passwd = ''.join(secrets.choice(potential_chars) for i in range(num_chars-2))
    passwd += secrets.choice(string.digits)
    passwd += secrets.choice(string.ascii_uppercase)

    result = random.sample(passwd, k=len(passwd))
    random.shuffle(result)
    passwd = ''.join(result)

    return passwd


# create a temporary password
print(generate_temp_pass(10))

# create a stronger temporary password
print(generate_better_pass(10))

# create a temporary, hard-to-guess URL
result_url = "https://my.example.com?reset="
result_url += secrets.token_urlsafe(15)
print(result_url)
