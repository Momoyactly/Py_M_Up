import csv
import os
import calendar

m =[]
with open(os.getcwd() + "/PyBank/Resources/budget_data.csv", mode='r') as csv:
    for counter, row in enumerate(csv):
        m.append(row.split(","))

headers = m[0]
m.pop(0)
csv_in_array = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))] 
for i, profit_in_month in enumerate(csv_in_array[1]):
   csv_in_array[1][i] = int(profit_in_month[:-2])


first_month, first_year = csv_in_array[0][0].split("-")
last_month, last_year   = csv_in_array[0][-1].split("-")
Analysis = ["Financial Analysis", "----------------------------"]
Analysis.append("Total months: "+str(list(calendar.month_abbr).index(last_month)
                                + 12*int(last_year)
                                - list(calendar.month_abbr).index(first_month)
                                - 12*int(first_year)
                                + 1))


Analysis.append("total: $"+str(sum(csv_in_array[1])))

Analysis.append("Average Change: $"
                + str(sum(csv_in_array[1])/len(csv_in_array[1])))

Analysis.append("Greatest Increase in Profits: "
    + csv_in_array[0][csv_in_array[1].index(max(csv_in_array[1]))] + " $("
    + str(csv_in_array[1][csv_in_array[1].index(max(csv_in_array[1]))])+")")

Analysis.append("Greatest Increase in Profits: "
    + csv_in_array[0][csv_in_array[1].index(min(csv_in_array[1]))] + " $("
    + str(csv_in_array[1][csv_in_array[1].index(min(csv_in_array[1]))])+")")

with open(os.getcwd() + "/PyBank/Analysis/Analysis.txt","w+") as file:
    for row in Analysis :
        print(row)
        file.write(row +"\n")