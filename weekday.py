#Weekly Task 05
#Write a program that outputs whether or not today is a weekday.
#Author: Jarlath Scarry


import datetime as dt #import datetime as dt #https://www.programiz.com/python-programming/datetime

dayNumber = dt.date.today().weekday() #using today method of the date class of datetime module,
                                        #Then adding the weekday() gives the week dayNumber 0-6
                                        #https://stackoverflow.com/questions/29384696/how-to-find-current-day-is-weekday-or-weekends-in-python

if dayNumber < 5: # if the day number is less than 5 it is a week day (0 Mon,1 Tue, 2 Wed, 3 Thu, 4 Fri)
    print ("Yes, unfortunately today is a weekday") #print this out if above is true
    
else:  # if ti is day 5 or 6 it is the weekend (5 Sat, 6 Sun)
    print ("It is the weekend, yay!") #if the first condition is false (not a week day) then print this out

