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

# path to collect the data from the resources folder (3/Activities/08-Par_Wrestling)
budget_csv = os.path.join('PBResources', 'budget_data.csv')

# Defining the function and have it accept 'budget_data' as its sole parameter
def print_summary(budget_data):
    date = str(budget_data[0])
    profit_loss = int(budget_data[1])
    month_change = int(budget_data[3])

    # total months is the sum of the 'Date' column [0]
    total_months = len(list(budget_data[0]))

    # total is the total of the 'Profit/Losses' column [1]
    profit_loss_total = sum(budget_data[1])

    # month change needs to be created and the column appended to budget_data
    # month change is ('Profit/Losses' value 2) minus ('Profit/Losses value 1)
    month_change =

    # average change is (sum of month_change) divided by (count of month_change)
    avg_change = 

    # greatest increase in profits is the max value of month_change
    great_inc = max(month_change)

    # greatest decrease in profits is the min value of month_change
    great_dec = min(month_change)

    # print out the budget data stats that are calculated above
    print(f"Financial Analysis")
    print(f"------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: {profit_loss_total}")
    print(f"Average Change: {avg_change}")
    print(f"Greatest Increase in Profits: {great_inc}")
    print(f"Greatest Decrease in Profits: {great_dec}")

# open and read the csv file
with open(budget_csv, 'r', encoding='utf-8') as csvfile:
    # split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    # remove header
    next(csvreader)
    for row in csvreader:
        print(print_summary)