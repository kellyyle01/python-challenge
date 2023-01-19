# import os module firsT
import os

# import csv
import csv

election_csv = os.path.join(".", "Resources", "election_data.csv")

# Lists to store data
votes_total = 0
candidates= []

# Copy data from .csv into a list
with open (election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvfile)
    for row in csvreader:
        votes_total.append(row[2])

#total votes
        votes_total = votes_total + 1
        print(votes_total) 