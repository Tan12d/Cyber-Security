import random
import string
import pyautogui

chars = string.ascii_letters+string.digits
allchars = list(chars)

pw = pyautogui.password("Enter a password: ")
sample_pw=""

while(sample_pw!=pw):
    sample_pw = random.choices(allchars,k=len(pw))
    print("-->"+str(sample_pw)+"<--")
    if(sample_pw==list(pw)):
        print("The password is :"+"".join(sample_pw))
        break