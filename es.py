# Program that reads in a text file and outputs the number of e's it contains
#Author: Jaralth Scarry

fileName = input('Enter a file name (for example "alan"):')
fileName = fileName + ".txt"  #https://stackoverflow.com/questions/34442282/how-do-i-add-txt-on-the-end-of-a-users-input
#Assuming the file is in the same directory and is a text file, we just need to enter file name.

def letterFrequency(fileName, letter): #define function to return the letter count
    #https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/
    file = open(fileName, 'r') # open file in read mode
    text = file.read() # store content of the file in a variable
    return text.count(letter) # using count() function
 
numberOfe = letterFrequency(fileName,'e') # call the function to get the letter count for e and E
numberOfE = letterFrequency(fileName,'E') # and pass the counts into a variables to use later
eAndE = (numberOfe+numberOfE)

print('The letter "e" appears {} times in the file'.format(numberOfe))
print('The letter "E" appears {} times in the file'.format(numberOfE))
print('The total of all "E" upper and "e" lower case is: {}'.format(eAndE))


