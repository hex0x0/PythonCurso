import random

lowers = "abcdefghijklmnopqrstuvwxyz"
uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

numbers = "0123456789"
symbols = "@*#"

all = lowers + uppers + numbers + symbols

print(all)



pwd = ""


for i in range(0, len(all)):
    x = random.randint(0, len(all) - 1)
    pwd += all[x]

print(pwd)