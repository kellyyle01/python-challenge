# import os module firsT
import os

# import csv
import csv

budget_csv = os.path.join(".", "Resources", "budget_data.csv")

# Lists to store data
total_months = 0
net_total = 0
changes = []
greatest_increase = []
greatest_decrease = []

hobbies= ['picnics', 'biking']
print (hobbies[0])
# with open(budget_data) as csvfile:
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row
    header = next(csvreader)
    for clmn in csvreader:
        # total number of months in data set
    

        # net total amt of profit/losses over entire period
        print (clmn[1])
        net_total = net_total + int(clmn[1])

        # changes in profits/losses over entire period and average of changes
        # Loop through a range of numbers 

       # changes = [net_total[x+1] - net_total[x] for x in range(len(net_total)-1)]
        total_months= total_months + 1
        print(total_months) 

# ... and the average of those monthly differences.
    # changes = round(sum(changes) / int(len(changes)), 2)
    print("Average change is ")
    print (total_months)
    print (net_total)


 

        # greatest increase in profits (date and amt) over entire period
    

        # greatest decrease in profits (date and amt) over entire period
