import random


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
numeric = "0123456789"
size = int(input("Şıfre uzunluğu:"))
reqem = int(input("Şıfrede rakam sayı:"))
passw = "".join(random.sample(alphabet,size))
passw1 = "".join(random.sample(numeric,reqem))

son = passw + passw1
print("".join((random.choice(son) for i in range(size))))



