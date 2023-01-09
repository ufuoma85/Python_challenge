import csv
import os

election_data_csv = os.path.join( "Resources", "election_data.csv")
Pypoll_output = os.path.join( "Analysis", "election_output.csv")


#declaring parameters
total_votes = 0
#Initialing Candidates count
count_charles = 0 
count_diana = 0 
count_raymon = 0

with open(election_data_csv) as election_data: 
    reader = csv.reader(election_data)
    next(reader)

    first_row = next(reader)
    total_votes += 1
    
#counting each candidates votes
    
    for row in reader:
       
        total_votes = total_votes + 1
       
        if row[2] == "Charles Casper Stockham":
            count_charles += 1
        elif row[2] == "Diana DeGette":
            count_diana += 1
        elif row[2] == "Raymon Anthony Doane":
            count_raymon += 1
    
    outcome =  {"Charles": count_charles, "Diana DeGette": count_diana, "Raymon": count_raymon}      
#Calculating the Percentages
    percent_charles = round((count_charles / total_votes) * 100, 2)
    percent_diana = round((count_diana / total_votes) * 100, 2)
    percent_raymon = round((count_raymon / total_votes) * 100, 2)

    winner = max(outcome, key=outcome.get)
#Output Summary
output =f""" 
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
Charles Casper Stockham: {percent_charles}% ({count_charles})
Diana DeGette: {percent_diana}% ({count_diana})
Raymon Anthony Doane: {percent_raymon}% ({count_raymon})
-------------------------
Winner: {winner}
"""

print (output)

with open(Pypoll_output, "w") as txt_file:
    txt_file.write(output)
