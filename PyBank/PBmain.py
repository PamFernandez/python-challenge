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


# following code from 3/Activities/01-Stu_CerealCleaner/Solved
# open and read csv
with open(budget_csv, 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # remove header
    next(csvreader)
    for row in csvreader:

    # find total for profit_loss
    sum = 0
    for sum in profit_loss:
    sum = sum + profit_loss
    print(sum)
