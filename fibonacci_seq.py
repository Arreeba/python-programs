#fibonacci sequence: starts 1,1,2,3,5,8,....Each number in sequence (after the
#first two)is sum of the previous two. This is a program that computes and outputs
#the nth Fibonacci number.

n=eval(input("enter the nth term: "))
a=1
b=1
if n==1 or n==2:
    print("The nth term is 1")
else:
    for i in range(n-2):
        c=a+b
        a=b
        b=c
    print("The",n,"th term is:", c)
