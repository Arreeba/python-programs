#The speeding ticket fine policy in Podunksville is $50 plus $5 for each mph over the limit plus
#a penalty of $200 for any speed over 90 mph. Here is a program that accepts a speed limit
#and a clocked speed and either prints a message indicating the speed was legal or prints the
#amount of the fine, if the speed is illegal.

#my solution:

#speed_limit=eval(input("enter a speed limit: "))
#users_speed=eval(input("enter a speed: "))
#difference=users_speed-speed_limit
#if users_speed>90 and users_speed>speed_limit:
 #   fine=50+5*difference+200
  #  print("fine is",fine)
#elif users_speed>speed_limit:
 #   fine=50+5*difference
  #  print("fine is",fine)
#else:
 #    print("no fine")
 
 #Modified Version: it also avoids repitition of fine calculations and is short.
 
speed_limit = int(input("Enter the speed limit: "))
clocked_speed = int(input("Enter the clocked speed: "))

if clocked_speed <= speed_limit:
    print("Speed was legal.")
else:
    fine = 50 + (clocked_speed - speed_limit) * 5
    if clocked_speed > 90:
        fine += 200
    print("Fine amount: ${:.2f}".format(fine))

                 
                 
        
    
    
        
