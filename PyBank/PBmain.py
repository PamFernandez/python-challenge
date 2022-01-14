# calculate the total number of months included in the datase
# calculate the net total amount of "profit/losses" over the entire period
# calculate the total amount of "profit/losses" over the entire period
#   then find the average of those changes
# calculate the greatest increase in profits (date and amount) ovetr the entire period
# calculate the greatest decrease in profits (date and amount) ovetr the entire period
#
# for example:
# Financial Analysis
# ------------------
# Total Months: 86
# Total: $38382578
# Average Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($2196167)
# 
# The final script should both print the analysis to the terminal and export a text file with the results

import os
import csv

# path to collect the data from the resources folder
budget_csv = os.path.join('PBResources', 'budget_data.csv')

# following code from 3/Activities/08-Par_Wrestling/Solved
# define the function and have it accept 'budgetdata' as its sole parameter
def print_analysis(budgetdata):
    total_months = str(budgetdata[0])
    total = int(budgetdata[1])
    avg_change = int(budgetdata[2])
    great_inc = int(budgetdata[3])
    great_dec = int(budgetdata[4])

    # total_months can be found by summing 'Date'
    total_months = sum(budget_csv[0])

print(sum(total_months))

#     # total can be found by summing "Profit/Losses"
#     total_pl = sum('Profits/Losses')

#     # avg_change can be found by dividing total_pl by total_months
#     avg_change = (total_pl / total_months)

#     # greatest increase can be found by 
#     #great_inc =

#     # greatest decreas can be found by
#     #great_dec =

#     # print the analysis
#     print(f"Financial Analysis")
#     print(f"------------------")
#     print(f"Total Months: {total_months}")
#     print(f"Total: {total_pl}")
#     print(f"Average Change: {avg_change}")
#     print(f"Greatest Increase in Profits: {great_inc}")
#     print(f"Greatest Decrease in Profits: {great_dec}")

# # following code from 3/Activities/01-Stu_CerealCleaner/Solved
# # open and read csv
# with open(budget_csv, 'r', encoding='utf-8') as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=',')
    
#     # read the header row first
#     header = next(csvreader)

# # print the analysis    
    
#     print(f"Financial Analysis")
#     print(f"------------------")
#     print(f"Total Months: {total_months}")
#     print(f"Total: {total_pl}")
#     print(f"Average Change: {avg_change}")
#     print(f"Greatest Increase in Profits: {great_inc}")
#     print(f"Greatest Decrease in Profits: {great_dec}")

