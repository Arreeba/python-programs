#A program that accepts a string of comma separated passwords from the user and
#checks their validity against a specific set of critirea and prints out the valid
#ones only.
import re
user_password=input("Please enter comma separated passwords: ")
valid_password=[]
for password in user_password.split(","):
        if (len(password)<12 or len(password)>25):
            continue
        elif not re.search("[a-z]",password):
            continue
        elif not re.search("[0-9]",password):
            continue
        elif not re.search("[A-Z]",password):
            continue
        elif not re.search("[@gmail.com]",password):
            continue
        else:
                valid_password.append(password)
Strvalid_password=",".join(valid_password)                
print(Strvalid_password)
                
                
                
            
            
            
