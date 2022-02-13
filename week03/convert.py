#Answer to Lab3.2 Question 4
#Program makes absolute cents
#Author: Jarlath

number = float(input("enter a number:\n"))
centValue = (number)*100  #equating the variable number to the absolute value of number
absoluteCents = (abs(int(centValue)))

print ("the absolute cents value of {} is {}".format(number,absoluteCents))
