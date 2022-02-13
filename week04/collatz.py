#collatz
#author: Jarlath Scarry

#Write a program that asks the user to input any positive integer and outputs the successive 
#values of the following calculation.
#At each step calculate the next value by taking the current value and, if it is even, 
#divide it by two, but if it is odd, multiply it by three and add one.
#Have the program end if the current value is one.
#$ python collatz.py
#Please enter a positive integer: 10
#10 5 16 8 4 2 1


any = 
#while val != "q":
if (any% 2) == 0:
    #print ("{} is an even number".format(any))

else:
    #print("{} is an odd number".format(any))
    #val = input ("(q to quit):")
#print ("Goodbye")

#https://stackoverflow.com/questions/61659143/how-do-i-divide-a-number-by-two-multiple-times/61659290
num = int(input("Please input any positive integer (press q to quit): (q to quit)"))
if num > 100 or num < 1:              # 2
    print("Error!")                   # 3
else:                                 # 4
    times = 0                         # 5
    while num >= 2:                   # 6
        num /= 2                      # 7
        times += 1                    # 8
    print(times)                      # 9


#number = float(input("enter a number:\n"))
#absoluteValue = (abs(number))  #equating the variable number to the absolute value of number
#print ("the absolute value of {} is {}".format(number,absoluteValue))


print ('quit')