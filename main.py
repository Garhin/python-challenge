import os
import csv

# path to collect data from the Resources folder
csvpath = os.path.join('budget_data.csv')
csv_output =os.path.join("results.txt")

with open(csvpath) as csvfile:
      reader = csv.reader(csvfile)
      header =next(reader)
      total_months = 0
      total_profit_loss = 0
      total_sum = 0
      prev_profit_loss = 0
      greatest_increase = ["",0]
      greatest_decrease = ["" ,9999999]
      profit_loss_change = []
      for row in reader:   
      
         total_months = total_months + 1
         total_sum = total_sum + int(row[1])
         net_change =int(row[1]) - prev_profit_loss
       # Keep track of changes
         profit_loss_change += [net_change]
         print(profit_loss_change)

       # Reset values of prev_profit_loss to complete row
         prev_profit_loss = int(row[1]) 
         print(prev_profit_loss)


       # Greatest increase in profit (date and amount) over entire period increase_profit = total_profit - int(row[1])
#           if (profit_loss_change > greatest_increase[1]):
         greatest_increase[1] =profit_loss_change
         greatest_increase[0] =row[1]

         if (net_change > greatest_decrease[1]):

           greatest_decrease[1] =profit_loss_change
           greatest_decrease[0] =row[1]
            #Add to profit_loss_changes list
           profit_loss_change.append(int(row["profit/losses"]))

          #Create the profit loss average
        
profit_loss_avg = sum(profit_loss_change) / len(profit_loss_change)


# Print 

print("Financial Analysis")
print("--------------")
print("Total Months: " +str(total_months))
print("Total : " + "$" + str(total_sum))
print("Average Change: " + "$" + str(round(profit_loss_avg, 2)))
print("Greatest Increase: " + str(greatest_increase[0]) + "$" + str(greatest_increase[1]))
print("Greatest Decrease: " + str(greatest_decrease[0]) + "$" + str(greatest_decrease[1]))



# #Output Files
with open(csv_output, "w") as txt_file:

            txt_file.write("Total Months: " + str(total_months))
            txt_file.write("\n")
            txt_file.write("Total: " + "$" + str(total_months))
            txt_file.write("\n")
            txt_file.write(str(profit_loss_avg))
            txt_file.write("Average Change" + str(round(profit_loss_avg, 2)))
            txt_file.write("\n")
            txt_file.write("Greatest Increase: " + str(greatest_increase))
            txt_file.write("\n")
            txt_file.write("Greatest decrease: " + str(greatest_decrease[0]) + "($" + str(greatest_decrease[1]) + ")")
