#Weekly task 3
#Program that takes an sentence and will output every second letter in reverse order.
#Author: Jarlath

print ( 'Please enter the following sentence "The quick brown fox jumps over the lazy dog."')
yourSentence = str(input("Please enter the sentence:\n")) #Program to prompt the user for the sentence

yourSentenceReversed = (yourSentence[::-2]) #reverse and skip every second carachter

print (yourSentenceReversed)