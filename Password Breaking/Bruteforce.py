import random
import string

def crack_password(passwd):
    attempts = 0
    while True:
        guess = ''.join(random.choices(string.ascii_letters+string.digits,k=len(passwd)))
        attempts+=1

        if guess == passwd:
            return attempts
        
        if attempts % 100000 == 0:
            print(f"Attempt {attempts}: {guess}")
        
passwd = input("Enter the password  to crack: ")
print("Cracking password...")

attempts = crack_password(passwd)
print(f'The password was cracked in {attempts} attempts')