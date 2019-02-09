import csv
import os

pybank = "/Users/2fresh/Desktop/Working Repo & Notes/1) Homework Working Repo/Unit 3/Instructions/PyBank/Resources/budget_data.csv"

with open(pybank, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        total_month = sum(1 for row in reader)

with open(pybank, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        total_sum = sum(int(row[1]) for row in reader)

rows = []
rows_stagger = []

with open(pybank, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(csvfile)
    for row in reader:
        rows.append(int(row[1]))

with open(pybank, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(csvfile)
    next(csvfile)
    for row in reader:
        rows_stagger.append(int(row[1]))
        
diff = [x1-x2 for (x1,x2) in zip(rows_stagger, rows)]
diff_avg = (sum(diff))/(total_month -1)
        
with open(pybank, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        max_val = max(int(row[1]) for row in reader)

with open(pybank, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        max_month = [str(row[0]) for row in reader if int(row[1]) == max_val]

with open(pybank, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        min_val = min(int(row[1]) for row in reader)

with open(pybank, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        min_month = [str(row[0]) for row in reader if int(row[1]) == min_val]


print("Financial Analysis")
print("------------------------")
print(f"Total Months: {total_month}")
print(f"Total Sum: ${total_sum}")
print(f"Average Change: ${diff_avg}")
print(f"Greatest Increase In Profits: {max_month} ${max_val}")
print(f"Greatest Decrease In Profits: {min_month} ${min_val}")

output_path = "/Users/2fresh/Desktop/Working Repo & Notes/1) Homework Working Repo/Unit 3/Instructions/PyBank/Resources/results.csv"

with open(output_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(["Financial Analysis"])
    writer.writerow(["-----------------------"])
    
    writer.writerow(["Total Months:", str(total_month)])
    writer.writerow(["Total Sum:", str(total_sum)])
    writer.writerow(["Average Change:", str(diff_avg)])
    writer.writerow(["Greatest Increase In Profits:", str(max_month), str(max_val)])
    writer.writerow(["Greatest Decrease In Profits:", str(min_month), str(min_val)])