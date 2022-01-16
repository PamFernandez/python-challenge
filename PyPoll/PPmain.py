# The dataset is composed of three columns: Voter ID, County, and Candidate. 
# Your task is to create a Python script that analyzes the votes and calculates each of the following:

# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.
#
# As an example, your analysis should look similar to the one below:
# 
# Election Results
# -------------------------
# Total Votes: 3521001
# -------------------------
# Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
# -------------------------
# Winner: Khan
# -------------------------

# In addition, your final script should both print the analysis to the terminal and export a text file 
# with the results.

# import dependencies
import csv
import os

# variables
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0
other_votes = 0

# file path
csvpath = os.path.join("PPResources", "election_data.csv")
file_to_output = os.path.join("PPAnalysis", "election_analysis.txt")

# open and read the CSV file
with open(csvpath, "r", encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # skip the header row
    next(csvreader)
    # iterate through the file
    for row in csvreader:

        # The total number of votes cast
        # add one to the total_votes variable for each line in the reader
        total_votes += +1
        
        # A complete list of candidates who received votes        
        # add to the candidate's _votes variable each time the specified candidate's name appears in csvdata
        if (row[2] == "Khan"):
            khan_votes += 1
        elif(row[2] == "Correy"):
            correy_votes += 1
        elif(row[2] == "Li"):
            li_votes += 1    
        elif(row[2] == "O'Tooley"):
            otooley_votes += 1
        else:
            other_votes += 1
    
    # The percentage of votes each candidate won
    # (khan_votes / total_votes) - the times one-hundred part is in the output as ".3%"
    khan_percent = (khan_votes / total_votes)
    correy_percent = (correy_votes / total_votes)
    li_percent = (li_votes / total_votes)
    otooley_percent = (otooley_votes / total_votes)

    # The winner of the election based on popular vote.
    # make a list of the vote totals, winner is the one with the highest (max) number
    winner_list = max(khan_votes, correy_votes, li_votes, otooley_votes, other_votes)
    
    if winner_list == khan_votes:
        winner = "Khan"
    if winner_list == correy_votes:
        winner = "Correy"
    if winner_list == li_votes:
        winner = "Li"
    if winner_list == otooley_votes:
        winner = "O'Tooley"
    else:
        winner = "Other"

# print analysis
print("")
print(f"Election Results")
print(f"---------------------")
print(f"Total Votes: {total_votes}")
print(f"---------------------")
print(f"Khan: {khan_percent:.3%}, {khan_votes}") 
print(f"Correy: {correy_percent:.3%}, {correy_votes}") 
print(f"Li: {li_percent:.3%}, {li_votes}") 
print(f"O'Tooley: {otooley_percent:.3%}, {otooley_votes}") 
print(f"---------------------")
print(f"Winner: {winner}")
print(f"---------------------")
print("")

# create output to a text file
with open(file_to_output, 'w', newline='') as txtfile:
    txtfile.write(f"Election Results\n")
    txtfile.write(f"------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write(f"------------------------\n")
    txtfile.write(f"Khan: {khan_percent:.3%}, {khan_votes}\n") 
    txtfile.write(f"Correy: {correy_percent:.3%}, {correy_votes}\n") 
    txtfile.write(f"Li: {li_percent:.3%}, {li_votes}\n") 
    txtfile.write(f"O'Tooley: {otooley_percent:.3%}, {otooley_votes}\n") 
    txtfile.write(f"------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write(f"------------------------\n")
   