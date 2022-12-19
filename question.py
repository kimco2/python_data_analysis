# creating file paths across operating system and module for reading cs
import os
import csv

# where the csv file is stored
budget_csv = os.path.join('Resources', 'budget_data.csv')

# Define
total_months = 0
total_profit = 0

# set inital value for the sum of the change in profit to zero
sum_profit_change = 0

# set intial value for the average profit change to zero
average_change = 0

# create a list to hold the greatest increase and decrease date and profit values 
greatest_increase = ["", -100000000]
greatest_decrease = ["", 100000000]

# Open the CSV
with open(budget_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    
    # Read the header row first
    csv_header = next(csv_reader)
    # setting Jan-10 as the first row
    # first_row = next(csv_reader)
        
    # defining what the initial previous net value is (setting it as the Jan-10 profit $)
    # previous_net = int(first_row[1])
        
    # creating a list to hold the net change values
    # net_change_list = []

     # calculate total months
    for row in csv_reader:
        date = row[0]
        profit = int(row[1])

        # calcuating total number of months in file
        total_months += 1
        print(date)

        # calculating total profit by summing it together
        total_profit += profit
         
        # # calculating the net change in profit from one month to the next
        # net_change = int(row[1]) - previous_net
        # previous_net = int(row[1])
        
        #  # adding the net change value to the list created to hold the net change figures
        # net_change_list = net_change_list + [net_change]
        
        # # calculating the profit change by adding together the total net change values
        # sum_profit_change += net_change

        # # # adding value to the list created to hold the net change figures
        # # net_change_list = net_change_list + [net_change]
          
        # if net_change > greatest_increase[1]:
        #     greatest_increase[0] = date
        #     greatest_increase[1] = net_change

        # if net_change < greatest_decrease[1]:
        #     greatest_decrease[0] = date
        #     greatest_decrease[1] = net_change

       
    # # calcuating the average change in profit
    # average_profit_change = sum(net_change_list) / len(net_change_list)

    # greatest_increase_profit = max(net_change_list)
    # greatest_increase_index = net_change_list.index(greatest_increase_profit)


        

print("Financial Analysis")
print ("-----------------------------")
print("Total Months: " + str(total_months))
print("Total: $" + str(total_profit))
# print("Greatest Increase in Profits: " + greatest_increase[0] + " " + "($" + str(greatest_increase[1]) + ")")
# print("Greatest Decrease in Profits: " + greatest_decrease[0] + " " + "($" + str(greatest_decrease[1]) + ")")

