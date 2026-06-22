import random

low = "abcdefghijklmnopqrstuvwxyz"
up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
characters = low + up + num

len = int(input("enter tje length of the passowrd :"))

paswo = ""

for i in range(len):
    paswo += random.choice(characters)

passwo = list(paswo)
random.shuffle(passwo)

paswo= "".join(passwo)

print("the password iss :", paswo)