Weekly Task 03 and Lab3 extra questions answered.
author: Jarlath Scarry

Q1. Write a program that asks a user to input a string and outputs every second letter in reverse order.

secondstring.py added

reference: https://www.w3schools.com/python/python_howto_reverse_string.asp


Lab3.1 extra questions.
#Author: Jarlath

Q6. Why does this expression cause an error? How can you fix it? 
#message = 'I have eaten ' + 99 + ' burritos.'
#print (message)

This did not work because 99 is an int. Only a str can be added to a str with the operator + +

message = 'I have eaten ' + str(99) + ' burritos.'
print (message)

Q7. Why is eggs a valid variable name while 100 is invalid? 
#Variable names cannot begin with a number

Q8. What three functions can be used to get the integer, floating-point number, or string version of a value?

age = 10
print (int(age))

height = 1.8
print (float(height))

name = 'John'
print (str(name))

reference: https://www.digitalocean.com/community/tutorials/

Lab3.2 Extra question 
Q4.

convert.py added