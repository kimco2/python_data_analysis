# importing data file
import os
import csv
budget_csv = os.path.join('Resources', 'budget_data.csv')

# Track various financial paramaters
total_months = 0
total_net = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 99999999999]

# Read the csv file and convert it into a list of dictionaries
with open(budget_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
          
    # Read the header row first 
    csv_header = next(csv_reader)
   
    # extract first row to avoid appending to net_change_list
    first_row = next(csv_reader)
    previous_net = int(first_row[1])
       
    for row in csv_reader:
        date = row[0]
        profit_loss = row[1]

        # calcuating total months
        total_months += 1
     
        # calculating total profit
        total_net += int(profit_loss)

        # track net change
        net_change = int(row[1]) - previous_net
        previous_net = int(row[1])
        net_change_list.append(net_change)
      
        # calcuating the average change in profit
        average_profit_change = sum(net_change_list) / len(net_change_list)

        # calculate greatest increase
        if net_change > greatest_increase[1]:
            greatest_increase[0] = date
            greatest_increase [1] = net_change

        #calculte the greatest decrease
        if net_change < greatest_decrease[1]:
            greatest_decrease [0] = date
            greatest_decrease [1] = net_change

# print results to the terminal
print(f"Financial Analysis")
print (f"-----------------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: $ {str(total_net)}")
print(f"Average : $ {round(average_profit_change,2)}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${str(greatest_increase[1])})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${str(greatest_decrease[1])})")

# export the results to a text file
report = open('PyBank_report.txt', 'w')
report.write(f"Financial Analysis\n")
report.write(f"-----------------------------\n")
report.write(f"Total Months: {str(total_months)}\n")
report.write(f"Total: $ {str(total_net)}\n")
report.write(f"Average : $ {round(average_profit_change,2)}\n")
report.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${str(greatest_increase[1])})\n")
report.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${str(greatest_decrease[1])})\n")
report.close ()
