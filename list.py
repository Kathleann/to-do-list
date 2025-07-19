import os
os.system('cls')

print('Hello World')

# Kuadrat 
qr = [x ** 2 for x in range(1,21)]
print(qr)
# idk 
code = [x for x in range(1,31) if x % 3 == 0] 
print(code)
fruit = ["apel", "pisang", "jeruk", "semangka"]
long = [len(x) for x in fruit ]
print(long)
# sentence 
sent = "I don't like anything, even my own life."
tence = [x for x in sent if x in ['a','i','u','e','o']]
print(tence)
# fuck my life 
num = [10, -3, 5, -8, 0]
kucf = [x*2 for x in num if x in [10,5,0]]
print(list(kucf))