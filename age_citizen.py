#A person is eligible to be a US senator if they are at least 30 years old and have been a US
#citizen for at least 9 years. To be a US representative these numbers are 25 and 7, respectively.
#This is a program that accepts a person’s age and years of citizenship as input and outputs their
#eligibility for the Senate and House.

age=eval(input("enter your age: "))
years=eval(input("Enter years of citizenship: "))
if age>=30 and years>=9:
    print("You are eligible for both.")
elif age>=25 and years>=7:
     print("You are eligible for representative but not a senator.")
else:
     print("You are eligible for none.")
## Passes all tests:)YAY!!
