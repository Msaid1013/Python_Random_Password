import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIFJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()`~_-<>,.?/:;|[]{}'

length = int(input("What do you want your length to be: "))

passwords = “”

for i in range(length):
    passwords += random.choice(chars)
print("Here is your random password: ", passwords)
