import random
import string

length = int(input("Enter the desired length of your Password: "))

characters = string.ascii_letters + string.digits + string.punctuation

password = "".join(random.choice(characters)for _ in range(length))

print(f"Generated Password: {password}")