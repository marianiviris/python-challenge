# PYPOLL
import os
import csv

csvpath = "Resources/PyPoll_electiondata.csv"

total_votes = 0
candidates_unique = []
candidate_vote_count = []

with open(csvpath, 'r', newline='', encoding='utf8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)

    for row in csvreader:
        total_votes += 1
        candidate_in = (row[2])
        if candidate_in in candidates_unique:
            candidate_index = candidates_unique.index(candidate_in)
            candidate_vote_count[candidate_index] = candidate_vote_count[candidate_index] + 1
        else:
            candidates_unique.append(candidate_in)
            candidate_vote_count.append(1)

percentage = []
max_votes = candidate_vote_count[0]
max_index = 0

for x in range(len(candidates_unique)):
    vote_percentage = round(candidate_vote_count[x]/total_votes*100, 2)
    percentage.append(vote_percentage)
    
    if candidate_vote_count[x] > max_votes:
        max_votes = candidate_vote_count[x]
        max_index = x

election_winner = candidates_unique[max_index] 

# Print into terminal
print()
print()
print('Election Results')
print("--------------------------")
print(f'Total Votes: {total_votes}')
print("--------------------------")
for y in range(len(candidates_unique)):
    print(f'{candidates_unique[y]} : {percentage[y]}% ({candidate_vote_count[y]})')
print("--------------------------")
print(f'Winner: {election_winner}')
print("--------------------------")
print()
print()

# Print into new text document
output_file = "Resources/PyPoll_electionresults.txt"
with open(output_file, "w", newline="") as datafile:
    datafile.write('Election Results\n')
    datafile.write("--------------------------\n")
    datafile.write(f'Total Votes: {total_votes}\n')
    datafile.write("--------------------------\n")
    for y in range(len(candidates_unique)):
        datafile.write(f'{candidates_unique[y]} : {percentage[y]}% ({candidate_vote_count[y]})\n')
    datafile.write("--------------------------\n")
    datafile.write(f'Winner: {election_winner}\n')
    datafile.write("--------------------------")