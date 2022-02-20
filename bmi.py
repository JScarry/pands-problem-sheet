#Body mass index calculator
#Author: Jarlath Scarry

name = input ('Enter your name:')
print ('Hello {}\n Please answer the following questions and we\
    \n will calculate your Body Mass Index (BMI)\n'.format(name))
# \n to move code (and print out) onto next line

age = input ('What is your age?:')
#added age here. may use it later

weight = float(input ('What is your weight(KG)?:'))
height = float(input ('What is your height(CM)?:'))
# used float instead of int incase not whole numbers entered,eg weitht 82.5kg

print ('Your age is {} , weight {}KG and height is {}CM.\n'.format(age, weight, height))

#began working on confirmation here but # out
#ans = input ('Are these details correct? y/n\n')
#print (ans)

bmi = weight / (height/100)**2
print ('{} your BMI is {:.2f}' .format(name,bmi))
#print out bmi to 2 decimal places





