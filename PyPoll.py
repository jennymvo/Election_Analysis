#The data we need to retrieve.
#1. The total number of votes cast
#2. A complete list of candidates who recieve votes
#3. The percentate of votes each candidate won
#4. The total number of votes each candidate won. 
#5. The winner of the election based on popular vote. 

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1. Initialize a total vote counter:
totalVotes = 0

#Initialize candidates
candidate_options = []

#Initialize candidate voting dictionary
candidate_votes = {}

#Initiate winning candidate and winning count tracker
winning_candidate = ''
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    #Read and print the header row
    headers = next(file_reader)
    
    #print each row in the CSV file
    for row in file_reader:
        #2. Add to the total vote count. 
        totalVotes += 1

        #Print the candidate name from each row
        candidate_name = row[2]

        #Check if the candidate does not match any existing candidate 
        if candidate_name not in candidate_options:
            
            #Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            #2. Begin tracking the candidate's vote count
            candidate_votes[candidate_name] = 0

        #Add a vote to the candidates's count
        candidate_votes[candidate_name] += 1




#3. Print the total votes
print(totalVotes)

#print the candidate list. 
print(candidate_votes)

#Determine the percentage of votes for each candidate by looping through the counts. 
#1. Iterate through the candidate list. 
for candidate_name in candidate_votes:
    #2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    #3. Calculate the percentage of votes
    vote_percentage = float(votes) / float(totalVotes) * 100
      #  To do: print out each candidate's name, vote count, and percentage of
    # votes to the terminal.

    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name
    #4. Print the candidate name and percentage of votes
    print(f"{candidate_name}: recieved {vote_percentage:.1f}% ({votes:,})\n")
    
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)    