import csv
import os

m =[]
with open(os.getcwd() + "/PyBank/Resources/budget_data.csv", mode='r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csv_reader)
    for row in csvfile:
        date, profit = row.split(",")
        m.append([date,int(profit.replace("\n",""))])


csv_in_array = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))] 

Analysis = ["Financial Analysis", "----------------------------"]
Analysis.append(f"Total months: {len(csv_in_array[0])}")
Analysis.append(f"Total: $ {sum(csv_in_array[1])}")
Analysis.append(f"Average Change: ${sum(csv_in_array[1])/len(csv_in_array[1])}")

greatest = []
i_Max_increase = csv_in_array[1].index(max(csv_in_array[1]))
i_Min_decrese = csv_in_array[1].index(min(csv_in_array[1]))
greatest.append([csv_in_array[0][i_Max_increase],csv_in_array[1][i_Max_increase]])
greatest.append([csv_in_array[0][i_Min_decrese],csv_in_array[1][i_Min_decrese]])

Analysis.append(f"Greatest Increase in Profits: {greatest[0][0]} $({greatest[0][1]})")
Analysis.append(f"Greatest decrese in Profits: {greatest[1][0]} $({greatest[1][1]})")

with open(os.getcwd() + "/PyBank/Analysis/Analysis.txt","w+") as file:
    for row in Analysis :
        print(row)
        file.write(row +"\n")