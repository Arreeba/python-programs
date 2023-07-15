#A program to check if an entered number>2 is prime. The program is also modified
#to find every prime number less than or equal to n.

import math
n=eval(input("Enter a positive whole number>2: "))
#checks the user input

while n<=2 or n<0:
    n=eval(input("Invalid number, Enter again: "))
d=2
while True:
    r=n%d
    if r==0:
       print(n,"is not prime")
       break
    if d>math.sqrt(n):
        print(n,"is a prime number")
        break
    d=d+1
#modification of program to print prime numbeers till n
print("Here are the prime numbers upto",n,":")    
for i in range (3,n+1):
    d=2
    while True:
        r=i%d
        if r==0:
            break
        if d>=math.sqrt(i):
            print(i)
            break
        d=d+1
