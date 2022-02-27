# Weekly task 6
# Author: Jarlath Scarry

#Write a program that takes a positive floating-point number 
#as input and outputs an approximation of its square root.

#def toPower(number, power = 3):   #power if not set is 3, or below toPower(5 ,2) is to the power of 2
    #print(number)
    #return number ** power


#num = 9

#print ( num, "to the power of 3 is", toPower (num))
###answer = toPower(5 , 2)
#print (answer)

import math
num1 = input("enter a number:")
def sqRt(num1):
    return math.pow(num1, 0.5)

print ( "Square root of {} is {}",format (num1, num1(sqRt)))

#https://flexiple.com/square-root-in-python/
#num = float(input(" Enter a number: "))
#sqRoot = math.pow(num, 0.5)
#print("The square root of a given number {0} = {1}".format(num, sqRoot))
