#Algorithn to estimate square root using Newton's method.
#Author: Jarlath Scarry

# Square Root of a Number using Newton's Method 
# | Python | 
# The Last Minute Professor
#https://www.youtube.com/watch?v=xdlIFw5EM4w

num = float(input("Enter a number:")) #read number in as a float

def sqrt(number): #define the function sqrt
    approx = 0.5*number #guess square root is 1/2 the number
    better = 0.5*(approx+number/approx) #run formula to get better guess
    while (better!=approx): #while loop to repeat guess until approx and better guess are equal
        approx = better #make approx equal to better  
        better=0.5*(approx+num/approx) #run formula to get better guess
    return better # return the result. (This could be approx, or better since the loop runs until both are equal)

answer = sqrt(num) #run the function
print("Squareroot of",num,"is:",answer) #print the answer

