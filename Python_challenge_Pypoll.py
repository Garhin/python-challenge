import os
import csv

# path to collect data from the Resources folder
csvpath=os.path.join('election_data.csv')
csv_output =os.path.join("results.txt")

with open(csvpath) as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        vote = 0
        winner_votes = 0
        winner = ""
        candidate_options = []
        candidate_votes = {}
        candidate_per = {}
        for row in reader:

                vote = vote + 1
               
                if row[2] not in candidate_options:
                        candidate_options.append(row[2])
                        candidate_votes[row[2]] = 0

                candidate_votes[row[2]] = candidate_votes[row[2]] + 1
        print("Election Results")
        print("-----------------------")
        print(vote)
        print(candidate_votes)
        # print("Winner: " + str(winner[1]))
        print("-----------------------")        

        for x in candidate_votes:
                # Determine the winner:
                candidate_per[x] =str(round(candidate_votes[x] / vote *100,2 )) + "%"
                if (candidate_votes[x] > winner_votes):
                        winner_votes = candidate_votes[x]
                        winner = x
                print(x,candidate_per[x],candidate_votes[x])        


       
                    #Output Files
with open(csv_output, "w") as txt_file:

            txt_file.write("Election_Results")
            txt_file.write("\n")
            txt_file.write("----------------------")
            txt_file.write("\n")
            txt_file.write(str(candidate_per))
            txt_file.write(str(winner))
            txt_file.write("\n")
            txt_file.write("----------------------")
            txt_file.write("\n")
            txt_file.write("Winner: " + str(winner[1]))
            txt_file.write("\n")
            txt_file.write("Total Votes " + str(vote))



