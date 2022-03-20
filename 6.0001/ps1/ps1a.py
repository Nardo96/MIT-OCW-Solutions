# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 15:52:14 2019

@author: Bernardo
"""
annual_salary = float(input("What is your annual salary? "))
portion_saved = float(input("How portion of your salary do you save? "))
total_cost = float(input("What is the cost of your dream home? "))

portion_down_payment = .25
current_savings = 0.0
r = .04 #Annual rate

number_of_months = 0

while current_savings < total_cost*portion_down_payment :
    current_savings += current_savings*r/12 + portion_saved*annual_salary/12
    number_of_months += 1

print("Number of months :" + str(number_of_months))