import random
import string

def crack(passwd):
    att = 0

    while True:
        att+=1
        guess = ''.join(random.choices(string.ascii_letters+string.digits,k=len(passwd)))

        if guess == passwd:
            return att
        
        if att % 100000 == 0:
            print(f'Attempts {att}: {guess}')

passwd = input("Enter the password: ")
print("Password is cracking...")

attempts = crack(passwd)
print(f'No. of attempts: {attempts}')