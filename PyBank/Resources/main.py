import os
import csv

# Set path for file
csvpath = os.path.join("budget_data.csv")

# Set Variables
total_number_months = 0
total_profit_losses = 0
previous_profit_losses = 0
change_profit_losses = 0
change_list = []
greatest_increase = ["",0]
greatest_decrease = ["", 9999999]

# Read in the CSV file
with open(csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    # Read each row first (skipthis step if there is now header)
    header = next(csvreader)
    first_row = next(csvreader)
    total_profit_losses = int(first_row [1])
    previous_profit = int(first_row [1])  

    #Loop through data
    for row in csvreader:

        # calculate totals
        total_number_months = total_number_months + 1
        total_profit_losses = total_profit_losses + int(row[1])
     
        # calculate changes
        change_profit_losses = int(row[1]) - previous_profit
        previous_profit = int(row[1])
        change_list.append(change_profit_losses)
        if change_profit_losses > greatest_increase [1]:
            greatest_increase[0] = row [0]   
            greatest_increase [1] = change_profit_losses
        if change_profit_losses < greatest_decrease [1]:
            greatest_decrease [0]= row[0]
            greatest_decrease [1] = change_profit_losses
 
 # calculate average
average = sum(change_list)/(len(change_list))
#print out Financial Analysis
print("Financial Analysis")
print("---------------------------")
print("total_number_months:" + str(total_number_months)) 
print("total_profit_losses:" + "$" + str(total_profit_losses))   
print("Average Change:" + "$" +str(change_profit_losses))
print("greatest increase:" + str(greatest_increase[0]) +  " ($" + str(greatest_increase[1]) + ")")
print("greatest_decrease:" + str(greatest_decrease[0]) + " ($" + str(greatest_decrease[1]) + ")")
