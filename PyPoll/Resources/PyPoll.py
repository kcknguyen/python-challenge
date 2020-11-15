import os
import csv

# Set path for file
csvpath = os.path.join("election_data.csv")

#Set Variable
total_votes = 0
list_of_candidates = 0
total_winner_vote = 0
popular_vote = 0

# open csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)
    first_row = next(csvreader)

    # loop through 
    for row in csvreader:

        #tally number of vote
        total_votes = total_votes + 1