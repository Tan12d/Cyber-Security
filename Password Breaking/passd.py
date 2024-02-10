from string import *
from itertools import product

value1 = ascii_letters
print(f'value1 = {value1}')
value2 = digits
print(f'value2 = {value2}')
value3 = punctuation
print(f'value3 = {value3}')


value = value1+value2+value3
print(f'value = {value}')
print(f'Length of value = {len(value)}')

for i in range(1,4):
    for j in product(value,repeat=i):
        word = "".join(j)
        p=open("password.txt","a")
        p.write(word)
        p.write("\n")
