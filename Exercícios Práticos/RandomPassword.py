import random

lowers = "abcdefghijklmnopqrstuvwxyz"
uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

numbers = "0123456789"
symbols = "@*#"

all = lowers + uppers + numbers + symbols

print(all)

length = 16

password = "".join(random.sample(all, length))

print(password)