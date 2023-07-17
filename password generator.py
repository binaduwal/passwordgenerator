import random 
import string
def generate_pass(length):
    characters=string.ascii_letters+string.punctuation+string.digits
    password="".join(random.choice(characters) for _ in range(length))
    return password
print("generated password:",generate_pass(8))
