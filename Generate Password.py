import random

passlen = int(input("Enter the length of password : "))

S = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_*?{}"

P = "".join(random.sample(S,passlen))
print(P)