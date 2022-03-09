#Weekly task 4
#Author: Jarlath Scarry

#I worked with code from the following link
#https://www.webucator.com/article/collatz-conjecture-in-python/

numList = [] # make a list called numList

def collatz(num):  # defining collatz function (user defined function) https://www.w3schools.com/python/python_functions.asp
    
    while(num) > 1: # while loop (https://realpython.com/lessons/intro-while-loops-python/) 
                        # keep repeating if or else steps below while the answer is greater than 1
        numList.append(num) # append number to the numList 

        if(num) % 2 == 0: # if number is even,
            num = int(num / 2) # devide number by 2
        
        else: # otherwise (if number is odd), 
            num = int((3 * num) + 1) # multiply number by 3 and add 1

    else: # otherwise (if number is now equal to 1)..
        numList.append(num) # append number to the numList (this will put 1 at the end of the list as the last number)
#collatz function is now defined
 
def main(): #define the main function. This is the first piece of code to be run
    num = int(input('Input an integer: ')) #request user to input an integer and read it in as class integer
    collatz(num) #run the collatz function on the number that was input
#main function is now defined

main() #call the main function
print(*numList, sep=" ") # print the list. *unpacks the list and sep=" " seperates items with a blank space.
#print('Done!')
