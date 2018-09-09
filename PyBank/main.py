import os
import csv
#import file
budget = os.path.join('budget_data.csv')
#empty lists
listmonths = []
listrevenue = []
# Open and read csv
with open(budget,'r' ) as csvfile:
    csvread = csv.reader(csvfile)

    next(csvread, None)

    for row in csvread:
        listmonths.append(row[0])
        listrevenue.append(int(row[1]))

#loop through revenue
total_months = len(listmonths)
greatest_inc = listrevenue[0]
greatest_dec = listrevenue[0]
total_revenue = 0

for r in range(len(listrevenue)):
    if listrevenue[r] >= greatest_inc:
        greatest_inc = listrevenue[r]
        great_inc_month = listmonths[r]
    elif listrevenue[r] <= greatest_dec:
        greatest_dec = listrevenue[r]
        great_dec_month = listmonths[r]
    total_revenue += listrevenue[r]
#calculate average_change
average_change = round(total_revenue/total_months, 2)
# printing results to terminal
print("Financial Analysis")
print("--------------------------------------------")
print("Total Months: " + str(total_months))
print("Total: $" + str(total_revenue))
print("Average Change: $" + str(average_change))
print("Greatest Increase in Profits: " + great_inc_month + ' ($' + str(greatest_inc) + ')')
print("Greatest Decrease in Profits: " + great_dec_month + ' ($' + str(greatest_dec) + ')')

# creating the new txt file
new_file = os.path.join('pybankanalysis.txt')
with open(new_file, 'w') as writefile:
# writing the text file
    writefile.writelines("Financial Analysis \n")
    writefile.writelines("-------------------------------------------- \n")
    writefile.writelines("Total Months: " + str(total_months) + "\n")
    writefile.writelines("Total: $" + str(total_revenue) + "\n")
    writefile.writelines("Average Change: $" + str(average_change) + "\n")
    writefile.writelines("Greatest Increase in Profits: " + great_inc_month + ' ($' + str(greatest_inc) + ')'+ '\n')
    writefile.writelines("Greatest Decrease in Profits: " + great_dec_month + ' ($' + str(greatest_dec) + ')')
