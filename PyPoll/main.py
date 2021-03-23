import csv
import os

m =[]
with open(os.getcwd() + "/PyPoll/Resources/election_data.csv", mode='r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for counter, row in enumerate(csvfile):
        m.append(row.split(","))

Analysis = ["Election Results", "-------------------------"]
Analysis.append("Total votes: " + str(len(m)))
Analysis.append("-------------------------")

csv_in_array = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))] 

count_by_candidate = {}
for name in set(csv_in_array[2]):
    count_by_candidate[name[:-1]] = [csv_in_array[2].count(name),
        round((csv_in_array[2].count(name)/len(csv_in_array[2]))*100)]

max_votes = ["",0]
for candidate, value in count_by_candidate.items():
    if max_votes[1] < value[0]:
        max_votes[1] = value[0]
        max_votes[0] = candidate      
    Analysis.append(candidate + " " + str(value[1]) + "% ("+str(value[0])+")")

Analysis.append("-------------------------")
Analysis.append("Winner: " + max_votes[0])
Analysis.append("-------------------------")

with open(os.getcwd() + "/PyPoll/Analysis/Analysis.txt","w+") as file:
    for row in Analysis :
        print(row)
        file.write(row +"\n")