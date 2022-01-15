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

# import dependencies
import csv
import os

# files to load and output
file_to_load = os.path.join("PBResources", "budget_data.csv")
file_to_output = os.path.join("PBAnalysis", "budget_analysis.txt")

# variables
total_months = 0
profit_loss_total = 0
monthly_change = []
month_count = []
great_inc = 0
great_inc_month = 0
great_dec = 0
great_dec_month = 0

# open and read the CSV file
with open(file_to_load, 'r') as budget_data:
    reader = csv.reader(budget_data, delimiter=",")

    # read the header row
    header = next(reader)
    # skip the header row
    # next(reader)
    row = next(reader)
    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)

    # variables for calculations
    total_months += 1
    profit_loss_total += int(first_row[1])
    previous_row = int(row[1])
     
    # read each row of data
    for row in reader:
  
        # total number of 'Dates' (months)
        total_months += 1
        
        # total of all 'Profit/Losses'
        profit_loss_total += int(row[1])
        
        # each months change - used only for calculating average change
        each_month_change = int(row[1]) - previous_row
        monthly_change.append(each_month_change)
        month_count.append(row[0])
        
        # greatest increase
        if int(row[1]) > great_inc:
            great_inc = int(row[1])
            great_inc_month = row[0]
       
        # greatest decrease
        if int(row[1]) < great_dec:
            great_dec = int(row[1])
            great_dec_month = row[0]

    # GETTING THE WRONG NUMBER
    # average change can be found by dividing profit_loss by total_months - 1
    avg_change = sum(monthly_change) / (total_months)
    print(sum(monthly_change))

    highest = max(monthly_change)
    lowest = min(monthly_change)

# print analysis
print(f"Financial Analysis")
print(f"------------------")
print(f"Total Months: {total_months}")
print(f"Total: {profit_loss_total}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: {great_inc_month}, (${highest})")
print(f"Greatest Decrease in Profits: {great_dec_month}, (${lowest})")


# HAVEN'T TRIED THIS YET WANT TO GET THE CORRECT OUTPUT FIRST
# create output file

# with open(file_to_output, 'w', newline = '') as csvfile:
#     csvwriter = csv.writer(csvfile, delimiter = ",")
#     csvwriter.writerow(f"Financial Analysis")
#     csvwriter.writerow(f"------------------")
#     csvwriter.writerow(f"Total Months: {total_months}")
#     csvwriter.writerow(f"Total: {profit_loss_total}")
#     csvwriter.writerow(f"Average Change: {avg_change}")
#     csvwriter.writerow(f"Greatest Increase in Profits: {great_inc_month}, (${highest})")
#     csvwriter.writerow(f"Greatest Decrease in Profits: {great_dec_month}, (${lowest})")
