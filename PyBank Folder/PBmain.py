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

filepath = os.path.join(python-challenge/PyBank Folder/PBResources/budget_data.csv)
with open(filepath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

