#Lab3.1 extra questions.
#Author: Jarlath

# Q6. Why does this expression cause an error? How can you fix it? 
#message = 'I have eaten ' + 99 + ' burritos.'
#print (message)
# this did not work because 99 is an int. Only a str can be added to a str with the operator + +

message = 'I have eaten ' + str(99) + ' burritos.'
print (message)

#7. Why is eggs a valid variable name while 100 is invalid? 
#Variable names cannot begin with a number

#8. What three functions can be used to get the integer, floating-point number, or string version of a value?

age = 10
print (int(age))

height = 1.8
print (float(height))

name = 'John'
print (str(name))

reference: https://www.digitalocean.com/community/tutorials/how-to-convert-data-types-in-python-3