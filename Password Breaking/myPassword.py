import random
import string
import pyautogui

pw = pyautogui.password("Enter a password: ")
sample_pw = ""
plist = list(pw)
print(plist)

count = 0

while(sample_pw != pw):
    count+=1
    sample_pw = random.choices(plist,k=len(pw))

    if(sample_pw == list(pw)):
        print("The password is : "+"".join(sample_pw))
        print("No. of attempts: ",count)
        break
