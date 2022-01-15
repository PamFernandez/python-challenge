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

# files to load and output
file_to_load = os.path.join("PPResources", "election_data.csv")
file_to_output = os.path.join("PBAnalysis", "election_analysis.txt")

# variables
total_votes = 0
kahn_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# open and read the CSV file
with open(file_to_load, 'r', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # read the header row
    header = next(csvfile)
    # skip the header row
    # next(reader)
    row = next(csvreader)

    # variables for calculations 

    # read each row of data
    for row in reader:

        #calculate total number of votes
        total_votes = total_votes + 1
        print(total_votes)
        


