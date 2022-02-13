#input a string and I will output every second letter in reverse order.
#Author: Jarlath

print ( "Please enter the following sentence: The quick brown fox jumps over the lazy dog.")
#yourSentence = str(input("enter the sentence:\n")). ## this line out and added
#the one below to automatically enter the sentence

yourSentence = ("The quick brown fox jumps over the lazy dog.") #enter sentence automatically

yourSentenceReversed = (yourSentence[::-2]) #reverse and skip every second carachter

print (yourSentenceReversed)
