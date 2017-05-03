# DishScheduler
Python code to sort people for dishes given availability

Senario:
Dish Jobs are done 6 times a week, excluding saturday
There are 4 dishe Jobs each day, Lunch Clean Up, Lunch Set Up, Dinner Clean Up and Dinner Setup, with 2 people per job
No Lunch Set Up is done on Sunday

Memebers fill out a form designating their name and which Jobs they are available.
Each member does a number of Dish Jobs defined in people_count.txt

Problem:
With this information, Create all possible combinations of who works what job where each person does the number of Jobs
Specified, and all Jobs are assigned.

Input:
there are two input files, people_count.txt and responses.

people_count.txt is formated so each line is of form
'''name number'''
where name is the name of a member and number is how many dishes they need to do

responses is formated that each line is of form
'''[first name] [last name] [[Day] [Job]]+''' 
