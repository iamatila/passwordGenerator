import random

print("Welcome to your Password Generator")

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?0123456789"

number = input("How many passwords do you want to generate?: ")
number = int(number)

length = input("How many characters should your password have?: ")
length = int(length)

print("\nHere are your passwords: ")

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)