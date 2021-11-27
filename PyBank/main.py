import os
import csv

#Get the CSV file
budget_file = os.path.join("budget_data.csv")
export_file = os.path.join("budget_analyis.txt")

#set variables with starting values
total_months = 0
total_revenue = 0
previous_net = 0

#create lists to hold values
month_of_change_list =[]
net_changes_list = []

#create lists with ranges for the increases and decreases
greatest_increase = ["", 0]
greatest_decrease = ["",9999999999999999999]


#convert file to dictionary so there will be headers and open the file with the reader
with open(budget_file) as monthly_pl:
    reader = csv.reader(monthly_pl)

    # tell the csv reader that there is a header and not to add it to the salient row values
    header = next(reader)
    first_row = next(reader)    
    total_months += 1

    #total revenue should be an integer so you can do math with it
    total_revenue += int(first_row[1])
    previous_net += int(first_row[1])

   

    #Loop through all the rows
    for row in reader:


        #count the number of months
        total_months += 1
        #total the revenue, reader interprets everything as a string by default so cast the revenue as an integer so it will total
        total_revenue += int(row[1])

        #track the net revenue changes and update the change lists
        #subtract the previous revenue from the value of the current row
        #then add the revenue change to the revenue change list
        net_change = int(row[1]) - previous_net
        previous_net = int(row[1])
        net_changes_list += [net_change]
        month_of_change_list += [row[0]]

        #calculate the greatest revenue increase
        #revenue change vs the current greatest increase at 1 is, if it's larger, update the array with the current increase & date
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase [1] = net_change

        #calculate the greatest revenue decrease, as above but looking for a decrease larger than the one currently stored in the array
        if net_change < greatest_decrease [1]:
            greatest_decrease[0] = row [0]
            greatest_decrease[1] = net_change

#calculate the average net change, the sum of the net changes divided by the number of months, ie the length of the net change list
net_monthly_avg = sum(net_changes_list)/len(net_changes_list)

#Print the outputs on the output text file in Analysis. Make it look like the example. 
output = (
    f"Financial Analysis\n"
    f"--------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_monthly_avg}\n"
    f"Average Change ${net_monthly_avg:2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

print(output)

#write the reports to the output text file
with open(export_file, "w") as txt_file: 
    txt_file.write(output)