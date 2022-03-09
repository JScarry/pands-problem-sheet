#Weekly task 2
#Body mass index calculator
#Author: Jarlath Scarry

name = input ('Enter your name:')
print ('Hello {}\n Please answer the following questions and we\
    \n will calculate your Body Mass Index (BMI)\n'.format(name)) # \n to move onto next line


weight = float(input ('What is your weight(KG)?:'))
height = float(input ('What is your height(CM)?:'))
# used float instead of int incase not whole numbers entered,eg weitht 82.5kg

print ('Your weight is {}KG and height is {}CM.\n'.format(weight, height))

bmi = weight / (height/100)**2 #calculation carried out on variables
print ('{} your BMI is {:.2f}' .format(name,bmi))
#print out bmi to 2 decimal places





