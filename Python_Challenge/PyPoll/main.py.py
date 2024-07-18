#!/usr/bin/env python
# coding: utf-8

# In[16]:


import os
import csv

# Joining path
budget_data_path = r"C:\Users\adolp\OneDrive\Desktop\Python_Challenge\PyBank\Resources\budget_data.csv"

# Open and read CSV
with open(budget_data_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    # Initialize variables
    total_months = 0
    net_total = 0
    previous_profit_losses = None
    changes = []
    dates = []
    
    # Process each row
    for row in csvreader:
        # Extract data
        date = row[0]
        profit_losses = int(row[1])
        
        # Update totals
        total_months += 1
        net_total += profit_losses
        
        # Calculate changes
        if previous_profit_losses is not None:
            change = profit_losses - previous_profit_losses
            changes.append(change)
            dates.append(date)
        
        previous_profit_losses = profit_losses

    # Calculate average change
    average_change = sum(changes) / len(changes)
    
    # Find greatest increase and decrease
    greatest_increase_value = max(changes)
    greatest_increase_date = dates[changes.index(greatest_increase_value)]
    greatest_decrease_value = min(changes)
    greatest_decrease_date = dates[changes.index(greatest_decrease_value)]

    # Print the results
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Net Total Profit/Losses: ${net_total}")
    print(f"Average Change: ${average_change:.2f}")
    print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_value})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_value})")

# Write results to a text file
output_path = r"C:\Users\adolp\OneDrive\Desktop\Python_Challenge\PyBank\analysis\PyBank.txt"
with open(output_path, "w") as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Net Total Profit/Losses: ${net_total}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_value})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_value})\n")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




