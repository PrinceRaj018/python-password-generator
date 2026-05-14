import random

characters = "abcdefghijklmnopqrstuvwxyz"
password = ""

length = int(input("Enter password length: "))

for i in range(length):
    password += random.choice(characters)

print(password)