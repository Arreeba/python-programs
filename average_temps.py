#Heating and cooling degree-days are measures used by utility companies to estimate energy
#requirements. If the average temperature for a day is below 60, then the number of degrees
#below 60 is added to the heating degree-days. If the temperature is above 80, the amount
#over 80 is added to the cooling degree-days.This program accepts a sequence of daily average
#temps and computes the running total of cooling and heating degree-days.

average_temps=eval(input("Enter a daily temp or -1 to quit: "))
heating_days=0
cooling_days=0
while average_temps!=-1:
    if average_temps<60:
        difference=60-average_temps
        heating_days+=difference
    if average_temps>80:
        diff_2=average_temps-80
        cooling_days+=diff_2
    average_temps=eval(input("Enter a daily temp or -1 to quit: "))
print("The total of heating days temps is:",heating_days)
print("The total of cooling days temps is:",cooling_days)
                         
