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
with open(file_to_load, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=",")

    # skip the header row
    next(reader)
    
    row = next(reader)
    
    # variables for calculations 
    total_months += 1
    profit_loss_total += int(row[1])
    previous_row = int(row[1])
     
    # read each row of data
    for row in reader:
  
        # calculate the total number of months included in the dataset
        total_months += 1
        
        # calculate the net total amount of "profit/losses" over the entire period
        profit_loss_total += int(row[1])
        
        # each months change - used only for calculating average change
        each_month_change = int(row[1]) - previous_row
        monthly_change.append(each_month_change)
        month_count.append(row[0])
        
        # calculate the greatest increase in profits (date and amount) over the entire period
        if int(row[1]) > great_inc:
            great_inc = int(row[1])
            great_inc_month = row[0]
       
        # calculate the greatest decrease in profits (date and amount) over the entire period
        if int(row[1]) < great_dec:
            great_dec = int(row[1])
            great_dec_month = row[0]

    # average change can be found by dividing profit_loss by total_months - 1
    avg_change = sum(monthly_change) / (total_months)

    highest = max(monthly_change)
    lowest = min(monthly_change)

# print analysis
print(f"Financial Analysis")
print(f"------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${profit_loss_total}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: {great_inc_month}, (${highest})")
print(f"Greatest Decrease in Profits: {great_dec_month}, (${lowest})")

# create output to a text file
with open(file_to_output, 'w', newline='') as txtfile:
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: {profit_loss_total}\n")
    txtfile.write(f"Average Change: {avg_change}\n")
    txtfile.write(f"Greatest Increase in Profits: {great_inc_month}, (${highest})\n")
    txtfile.write(f"Greatest Decrease in Profits: {great_dec_month}, (${lowest})\n")
