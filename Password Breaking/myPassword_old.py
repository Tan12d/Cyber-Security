import random
import string
import pyautogui

chars = string.ascii_letters+string.digits
allchars = list(chars)
print(allchars)
pw = pyautogui.password("Enter a password: ")
sample_pw = ""
plist = list(pw)
print(plist)
print('sample password\n')
count = 0

while(sample_pw != pw):
    count+=1
    sample_pw = random.choices(allchars,k=len(pw))
    print(str(sample_pw))
    if(sample_pw == list(pw)):
        print("The password is : "+"".join(sample_pw))
        print("No. of attempts: ",count)
        break
