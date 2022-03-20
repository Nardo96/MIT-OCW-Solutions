# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 16:13:24 2019

@author: Bernardo
"""

base_annual_salary = float(input("What is your annual salary? "))


semi_annual_rate = .07
r = .04
total_cost = 1000000.0
portion_down_payment = .25


epsilon = 100
low = 0
high = 10000
number_of_steps = 0

current_savings = 0.0
annual_salary = base_annual_salary
    
for month in range(36):
    current_savings += current_savings*r/12 + annual_salary/12
    if (month+1)%6 == 0:
        annual_salary += annual_salary*semi_annual_rate
            
if current_savings < (total_cost*portion_down_payment + epsilon): #Should be - epsilon
    print("It is not possible to pay the down payment in three years.")
    
else: 
    best_savings_rate = 0
    while (abs(current_savings - total_cost*portion_down_payment) > epsilon):
        current_savings = 0.0
        annual_salary = base_annual_salary
        best_savings_rate = (low + high)/2
        number_of_steps += 1
    
        for month in range(36):
            current_savings += current_savings*r/12 + float(best_savings_rate)/10000*annual_salary/12
       
            if (month+1)%6 == 0:
                annual_salary += annual_salary*semi_annual_rate
                
        if current_savings > total_cost*portion_down_payment:
            high = best_savings_rate
        elif current_savings < total_cost*portion_down_payment:
            low = best_savings_rate
        else: print("Found the perfect savings rate: " + str(float(best_savings_rate)/10000))
        
  
    print("Best savings rate: " + str(float(best_savings_rate)/10000))
    print("Number of steps: " + str(number_of_steps))
