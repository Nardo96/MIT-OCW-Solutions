# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 16:09:06 2019

@author: Bernardo
"""

annual_salary = float(input("What is your annual salary? "))
portion_saved = float(input("How portion of your salary do you save? "))
total_cost = float(input("What is the cost of your dream home? "))
semi_annual_rate = float(input("What is your semi-annual raise rate? "))

portion_down_payment = .25
current_savings = 0.0
r = .04 #Annual rate

number_of_months = 0

while current_savings < total_cost*portion_down_payment :
    current_savings += current_savings*r/12 + portion_saved*annual_salary/12
    number_of_months += 1
    if number_of_months%6 == 0:
        annual_salary += annual_salary*semi_annual_rate

print("Number of months :" + str(number_of_months))