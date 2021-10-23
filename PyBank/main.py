import os
import csv

#Get the CSV file
budget_file = os.path.join("Resources","budget_data.csv")
export_file = os.path.join("Analysis", "budget_analyis.txt")

#total number of months
total_months = 0
#total revenue
total_revenue = 0

#convert file to dictionary so there will be headers
with open(budget_file) as monthly_pl:
    reader = csv.reader(monthly_pl)

    # tell the csv reader that there is a header and not to add it to the salient row values
    header = next(reader)
    first_row = next(reader)    

    total_months += 1
    #total revenue should be an integer so you can do math with it
    total_revenue += int(first_row[1])


#Loop through all the rows
for row in reader:
    #count the number of months
    total_months += 1
    #total the revenue
    total_revenue += int(row[1])

    




output= ( 
    f"Financial Analysis\n"
    f"----------------------------------\n"
    f"Total Months: {total_months}\n"
)


print(output)


