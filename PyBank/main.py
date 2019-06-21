# PYBANK
import os
import csv

csvpath = "Resources/PyBank_budgetdata.csv"

with open(csvpath, 'r', newline='', encoding='utf8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)

    Date = []
    ProfLoss = []

    for row in csvreader:
        Date.append(row[0])
        ProfLoss.append(float(row[1]))    

    months = len(Date)
    SumProfLoss = sum(ProfLoss)

    AvgChange = []
    for i in range(1, months):
        AvgChange.append(ProfLoss[i]-ProfLoss[i-1])

    greatestIncProf = 0
    greatestDecProf = 0
    lowest_month = 0

    greatestIncProf = max(AvgChange)
    greatestDecProf = (min(AvgChange))
    greatest_month = Date[AvgChange.index(greatestIncProf) + 1]
    lowest_month = Date[AvgChange.index(greatestDecProf) + 1]
    

# Print into terminal
print()
print()
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {months}")
print(f"Total: ${SumProfLoss}")
print(f"Average Change: ${round(sum(AvgChange)/len(AvgChange))}")
print(f"Greatest Increase in Profits: {greatest_month} (${greatestIncProf})")
print(f"Greatest Decrease in Profits: {lowest_month} (${greatestDecProf})")
print()
print()

# Print into new text document
outputpath = "Resources/output_budgetdata.txt"
with open(outputpath, 'w', newline='') as datafile:
    datafile.write("Financial Analysis")
    datafile.write("----------------------------")
    datafile.write(f"Total Months: {months}")
    datafile.write(f"Total: ${SumProfLoss}")
    datafile.write(f"Average Change: ${sum(AvgChange)/len(AvgChange)}")
    datafile.write(f"Greatest Increase in Profits: {greatest_month} (${greatestIncProf})")
    datafile.write(f"Greatest Decrease in Profits: {lowest_month} (${greatestDecProf})")