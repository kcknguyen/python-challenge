# Modules
import os
import csv
# Set path for file
csvpath = os.path.join("..", "Resources", "election_data.csv")
# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")