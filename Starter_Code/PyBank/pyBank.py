import csv
import os

budget_data_csv = os.path.join( "Resources", "budget_data.csv")
Pybank_output = os.path.join( "analysis", "budget_output.csv")

#declaring parameters
total_months = 0
previous_revenue = 0
revenue_change_list = [] 
total_revenue = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999]

with open(budget_data_csv) as revenue_data: 
    reader = csv.reader(revenue_data)
    next(reader)

    first_row = next(reader)
    total_months += 1
    total_revenue += int(first_row[1])
    previous_revenue = int(first_row[1])

    
    for row in reader:
       
        total_months = total_months + 1
        total_revenue = total_revenue + int(row[1])

        revenue_change = int(row[1]) - previous_revenue
        previous_revenue = int(row[1])
        revenue_change_list.append(revenue_change) 
       
        #exit()

        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = revenue_change

        if (revenue_change > greatest_increase[1]):
            greatest_increase[0] = row[0]
            greatest_increase[1] = revenue_change

#Average Revenue Change
rev_average = sum(revenue_change_list) / len(revenue_change_list)

#Output Summary
output =f""" 
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total_revenue}
Average Change: ${rev_average:.2f}
Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})
Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})
"""

print (output)

with open(Pybank_output, "w") as txt_file:
    txt_file.write(output)


