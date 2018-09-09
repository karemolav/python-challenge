import os
import csv
#import file
election = os.path.join('election_data.csv')
candidates = {}
total_votes=0
# Open and read csv
with open(election,'r' ) as csvfile:
    csvread = csv.reader(csvfile)

    next(csvread, None)

    for row in csvread:
        total_votes += 1
        if row[2] in candidates.keys():
            candidates[row[2]] = candidates[row[2]] + 1
        else:
            candidates[row[2]] = 1
#create empty lists
names = []
count_votes = []

for dict, value in candidates.items():
    names.append(dict)
    count_votes.append(value)

percentagevote = []
for x in count_votes:
    percentagevote.append(round(x/total_votes*100,1))

summarize = list(zip(names, count_votes, percentagevote))
winner = []

for name in summarize:
    if max(count_votes) == name[1]:
        winner.append(name[0])
won = winner[0]

#creating the new txt file
new_file1 = os.path.join('pypollalysis.txt')

with open(new_file1, 'w') as writetxt:
# writing the text file
    writetxt.writelines('Election Results \n------------------------- \nTotal Votes: ' + str(total_votes) +
      '\n-------------------------\n')
    for entry in summarize:
        writetxt.writelines(entry[0] + ": " + str(entry[2]) +'%  (' + str(entry[1]) + ')\n')
    writetxt.writelines('------------------------- \nWinner: ' + won + '\n-------------------------')

# printing results to terminal
with open(new_file1, 'r') as readfile:
    print(readfile.read())
