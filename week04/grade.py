# This program reads in
# a students percentage
# and prints out the
# corresponding grade

percentageRaw = float(input("Enter the percentage (-1 to quit): (-1 to quit)"))
#quit function added to input

percentage = (round(percentageRaw))  
#round function added to round input to whole number
#then assign result to variable "precentage"

if percentage == -1:
    print ('End')
    #end when -1 is input
elif percentage < 0 or percentage > 100:
    print ("Please enter a number between 0 and 100")
    print ("{} rounded is {}" .format(percentageRaw,percentage))
    #Informs user what the input has been rounded to
    
elif percentage < 40: # we know it is greater than 0
    print ("{} is a Fail" .format (percentage))
elif percentage < 50: # between 40 and 49
    print ("{} is a Pass" .format (percentage))
elif percentage < 60: # between 50 and 59
    print ("{} is a Merit" .format (percentage))
elif percentage < 70: # between 60 and 69
    print ("{} is a Merit2" .format (percentage))
else:
    print ("{} is a Distinction" .format (percentage))

   
