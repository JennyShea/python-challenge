import os
import csv

#Get the CSV file
election_file = os.path.join("election_data.csv")
export_file = os.path.join("election_analyis.txt")

#set variables with starting values
total_votes = 0

#create lists to hold values
candidate_list =[]
candidate_votes_list = {}

#create variables for the winner info
winner = ""
winning_count = 0

#convert file to dictionary so there will be headers and open the file with the reader
with open(election_file) as election_data:
    reader = csv.reader(election_data)

    #Read the header
    header = next(reader)

    #Loop through all the rows
    for row in reader:

        #add the vote to the total vote count
        total_votes = total_votes + 1

        #Get the candidate name from that row and add it to the row list
        candidate_name = row[2]
        
        #if the name is not in the list then add it to the list and start tracking the total voter count
        if candidate_name not in candidate_list: 
            candidate_list.append(candidate_name)
            candidate_votes_list[candidate_name] = 0

        #add the vote on that row to the total
        candidate_votes_list[candidate_name] = candidate_votes_list[candidate_name] + 1


 #Print the results and export to to the text file

with open(export_file, "w") as txt_file: 
    all_votes = (
        f"\n\nElection Results \n"
        f"------------------------"
        f"Total Votes: {total_votes}\n"
        f"---------------------------\n"
    )
    print(all_votes)


    txt_file.write(all_votes)

    #find the winner, loop through the counts
    for candidate in candidate_votes_list: 

        #get the vote counts and then figure out the percentage. 
        votes = candidate_votes_list.get(candidate)
        vote_pc = float(votes) / float(total_votes) * 100

        #call the winner, the candidate with the most votes
        if (votes > winning_count):
            winning_count = votes
            winner = candidate 

        #Print the winner count and percentage
        winner_output = f"{candidate}: {vote_pc:.3f}% ({votes})\n"
        print(winner_output)

        #Add to the text file
        txt_file.write(winner_output)