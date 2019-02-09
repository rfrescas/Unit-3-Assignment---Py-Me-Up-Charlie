import csv
import os

pypoll = "/Users/2fresh/Desktop/Working Repo & Notes/1) Homework Working Repo/Unit 3/Instructions/PyPoll/Resources/election_data.csv"

with open(pypoll, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        total_votes = sum(1 for row in reader)

candidates_name = []

with open(pypoll, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(csvfile)
    for row in reader:
        if row[2] not in candidates_name:
            candidates_name.append(row[2])

count_candidate_1 = 0

with open(pypoll, 'r',) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        if row[2] == candidates_name[0]:
            count_candidate_1 += 1

perc_candidate_1 = round((count_candidate_1 / total_votes)*100, 1)

count_candidate_2 = 0

with open(pypoll, 'r',) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        if row[2] == candidates_name[1]:
            count_candidate_2 += 1

perc_candidate_2 = round((count_candidate_2 / total_votes)*100, 1)

count_candidate_3 = 0

with open(pypoll, 'r',) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        if row[2] == candidates_name[2]:
            count_candidate_3 += 1

perc_candidate_3 = round((count_candidate_3 / total_votes)*100, 1)

count_candidate_4 = 0

with open(pypoll, 'r',) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        if row[2] == candidates_name[3]:
            count_candidate_4 += 1

perc_candidate_4 = round((count_candidate_4 / total_votes)*100, 1)

counts_per_candidate = {}

with open(pypoll, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(csvfile)
    for row in reader:
        if row[2] not in counts_per_candidate:
            counts_per_candidate[row[2]] = 0
        counts_per_candidate[row[2]] = counts_per_candidate[row[2]] + 1

winner = max(counts_per_candidate, key=counts_per_candidate.get)
        
print("Election Results")
print("---------------------------")
print(f"Total Votes: {total_votes}")
print("---------------------------")
print("".join(candidates_name[0]), ":", f"{perc_candidate_1}%", f"({count_candidate_1})")
print("".join(candidates_name[1]), ":", f"{perc_candidate_2}%", f"({count_candidate_2})")
print("".join(candidates_name[2]), ":", f"{perc_candidate_3}%", f"({count_candidate_3})")
print("".join(candidates_name[3]), ":", f"{perc_candidate_4}%", f"({count_candidate_4})")
print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")

output_path = "/Users/2fresh/Desktop/Working Repo & Notes/1) Homework Working Repo/Unit 3/Instructions/PyPoll/Resources/results.csv"

with open(output_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(["Election Results"])
    writer.writerow(["---------------------------"])
    writer.writerow(["Total Votes:", str(total_votes)])
    writer.writerow(["---------------------------"])
    writer.writerow([str(candidates_name[0]), ":", str(perc_candidate_1), "%", str(count_candidate_1)])
    writer.writerow([str(candidates_name[1]), ":", str(perc_candidate_2), "%", str(count_candidate_2)])
    writer.writerow([str(candidates_name[2]), ":", str(perc_candidate_3), "%", str(count_candidate_3)])
    writer.writerow([str(candidates_name[3]), ":", str(perc_candidate_4), "%", str(count_candidate_4)])
    writer.writerow(["---------------------------"])
    writer.writerow(["Winner:", str(winner)])
    writer.writerow(["---------------------------"])