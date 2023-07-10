# program to check dates by user:

user=input("enter a date in form month/day/year: ")
user_input=user.split("/") # {'mm','dd','yyyy'}
months={'4','6','9','11'}
if eval(user_input[2])<1 or eval(user_input[0])<1 or eval(user_input[0])>12:
    print("invalid")
elif user_input[0] in months and user_input[1]=='31':
    print("Invalid input")
elif  user_input[0]=='2' and user_input[1]=='28' and eval(user_input[2])%4==0:
    print("Invalid date")
else:
    print("valid date")
