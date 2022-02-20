#Weekly task 4
#Author: Jarlath Scarry

#I worked with code from the following link
#https://www.webucator.com/article/collatz-conjecture-in-python/

def collatz(num):  #defining collatz function (user drfined function) https://www.w3schools.com/python/python_functions.asp
                   
    while(num) > 1: #while loop (https://realpython.com/lessons/intro-while-loops-python/) 
                        #keep repeating if or else steps below while the answer is greater than 1
        print(num) #print out the number at each step

        if(num) % 2 == 0: #if number is even,
            num = int(num / 2) #devide number by 2
        
        else: #otherwise (if number is odd), 
            num = int((3 * num) + 1) #multiply number by 3 and add 1

    else: #otherwise (if number is now equal to 1)..
        print(num) #print the number (this will print 1 since, while the number 
                    #is not equal to 1 the if or else step will still be executed)
        print('Done!') #Done! is printed after last step (when number is equal to 1)
                        #collatz function is now defined as the code between line 6 and 19. 
 
def main(): #define the main function. This is the first piece of code to be run
    num = int(input('Input an integer: ')) #request user to input an integer and read it in as class integer
    collatz(num) #run the collatz function on the number that was input
main() #end the main function
