# Import Dependencies
import os
import csv

# Declare file location through pathlib
input_file = os.path.join("Resources", "budget_data.csv")


# Create empty Lists to store data
sum_months = []
sum_profit = []
monthly_profit_change = []

with open(input_file, newline="", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header labels to iterate with the values
    header = next(csvreader)

    for row in csvreader:
        # Append the total months and total profit to their corresponding lists
        sum_months.append(row[0])
        sum_profit.append(int(row[1]))

    # Iterate through the profits in order to get the monthly change in profits
    for i in range(len(sum_profit)-1):

        # Take the difference between two months and append to monthly profit change
        monthly_profit_change.append(sum_profit[i+1]-sum_profit[i])

# Obtain the max and min of the the monthly profit change list
max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)


# We use the plus 1 at the end since month associated with change is the + 1 month or next month
max_increase_month = monthly_profit_change.index(
    max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(
    min(monthly_profit_change)) + 1

# Print Statements

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(sum_months)}")
print(f"Total: ${sum(sum_profit)}")
print(
    f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(
    f"Greatest Increase in Profits: {sum_months[max_increase_month]} (${(str(max_increase_value))})")
print(
    f"Greatest Decrease in Profits: {sum_months[max_decrease_month]} (${(str(max_decrease_value))})")

# Set variable for output file
output_file = os.path.join("text-file-analysis", "Financial_Analysis.txt")

#  Open the output file
with open(output_file, "w") as file:

    # Write in zipped rows
    # Write methods to print to Financial_Analysis
    file.write("Financial Analysis \n")
    file.write("---------------------------- \n")
    file.write(f"Total Months: {len(sum_months)}\n")
    file.write(f"Total: ${sum(sum_profit)}\n")
    file.write(
        f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}\n")
    file.write(
        f"Greatest Increase in Profits: {sum_months[max_increase_month]} (${(str(max_increase_value))})\n")
    file.write(
        f"Greatest Decrease in Profits: {sum_months[max_decrease_month]} (${(str(max_decrease_value))})\n")
