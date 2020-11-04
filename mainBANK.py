import os
import csv

# Send csv file data to the main folder
budget_r = os.path.join(".",'Resources', 'budget_data.csv')

# Create lists of for data from csv file
total_months = []
profit_losses = []
monthly_change = []
monthly_change_list=[]
 
# Open csv file
with open(budget_r,'r') as csvfiles:
     
    #CSV reader
    csvreader = csv.reader(csvfiles, delimiter =',')
    print(csvreader)
    #read header on first row
    csv_header = next(csvreader)
    
    for row in csvreader:
       
    # Enter total_months MONTHS  
        total_months.append(row[0])

    # Enter profit_losses REVENUE
        profit_losses.append(int(row[1]))

    #Enter average changes AVERAGE CHANGES
        i = 0
        for i in range (len(profit_losses)-1):
            monthly_change = [int(profit_losses[i+1]) - int(profit_losses[i])       
          
            #Append monthly change list
            monthly_change_list = append(monthly_change)

            #Calculate total monthly change
            total_monthly_change = sum(monthly_change_list)

            #Calculate average change
            average_change = total_monthly_change/len(monthly_change)

            #Calulate average change
            average_change = total_monthly_change/len(monthly_change)

            print(total_monthly_change)



            #Greatest Increase
            profit_increase = max(monthly_change) 
            print(profit_increase)

            x = monthly_change.index(profit_increase) 
            month_increase  = total_months[x +1]


            #Greatest Decrease
            profit_decrease = min(monthly_change)  
            y = monthly_change.index(profit_decrease)
            month_decrease = month[y+1]


        print(f'Financial Analysis' + '\n')
        print(f'-------------------' + '\n')

           
        print(f"Total number of months: " + str(len(total_months)))


        print(f"Total Revenue in period: $ " + str(total_revenue))


        print(f"Average monthly change in Revenue : $" + str(monthly_change))


        print(f"Greatest Increase in Profits: {month_increase} (${profit_increase})")


        print(f"Greatest Decrease in Profits: {month_decrease} (${profit_decrease})")



         

     





