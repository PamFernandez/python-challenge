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

# Dependencies
import csv
import os

# Files to load and output
file_to_load = os.path.join("PBResources", "budget_data.csv")
file_to_output = os.path.join("PBAnalysis", "budget_analysis.txt")

# Track various financial parameters
total_months = 0
monthly_change = []
month_count = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
profit_loss = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data, delimiter=",")

    # read the header row
    # header = next(reader)
    # skip the header row
    next(reader)
    row = next(reader)
    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)

    # variables for calculations
    total_months += 1
    profit_loss += int(first_row[1])
    previous_row = int(row[1])
    prev_net = int(first_row[1])
    
    # great_inc = 
    # great_dec = 
 
    # read each row of data
    for row in reader:
  
        # total number of 'Dates' (months)
        total_months += 1
        print(total_months)

        # total of all 'Profit/Losses'
        profit_loss += int(row[1])
        print(profit_loss)

        # months change - used only for calculating average change
        revenue_change = int(row[1]) - previous_row
        monthly_change.append(revenue_change)
        print(revenue_change) 
        month_count.append(row[0])
        # print(monthly_change)

        # GETTING THE WRONG NUMBER
        # average change can be found by dividing profit_loss by total_months - 1
        average_change = sum(monthly_change) / (total_months)
        print(average_change)
