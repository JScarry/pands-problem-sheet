# Program that reads in a text file and outputs the number of e's it contains
#Author: Jaralth Scarry

fileName =  "alan.txt" #Reading Parameters From a File - Python https://www.youtube.com/watch?v=fXrGfOS6lHk

def letterFrequency(fileName, letter): #define function to return the letter count
    #https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/
    file = open(fileName, 'r') # open file in read mode
    text = file.read() # store content of the file in a variable
    return text.count(letter) # using count() function
 
numberOfe = letterFrequency(fileName,'e') # call the function to get the letter count for e and E
numberOfE = letterFrequency(fileName,'E') # and pass the counts into a variables to use later
eAndE = (numberOfe+numberOfE)

print('The letter "e" appears {} times in the file "alan.txt"'.format(numberOfe))
print('The letter "E" appears {} times in the file "alan.txt"'.format(numberOfE))
print('The total of all "E" upper and "e" lower case is: {}'.format(eAndE))


