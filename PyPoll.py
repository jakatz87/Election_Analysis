#The data we need to retrieve.
#1. The total number of votes cast.
#2. A complete list of candidates recieving votes.
#3. The percentage of the vote that each candidate won.
#4. The total number of votes cast.
#5. The threshold for winning based on 50% +1
#6. The winner based on the threshold. 

#Add our dependencies
import csv
import os
#Assign a variable for the file to load and the path
file_to_load=os.path.join("Resources", "election_results.csv")

#Create a variable to save the file to a path.
file_to_save=os.path.join("analysis", "election_analysis.txt")

#Initialize the vote counter
total_votes=0

#Declare the candidate list
candidate_options=[]
#Declare the candidate vote total dictionary
candidate_votes = {}
#Winning Candidate and Winning Count Tracker
winning_cadidate = " "
winning_count=0
winning_percentage=0
#Open the election results and read the file
with open(file_to_load) as election_data:
    # Read and analyze the data here.
    file_reader=csv.reader(election_data)

    #Read the header row
    headers=next(file_reader)
    
    #Print each row in the file
    for row in file_reader:
        #Add to the total vote count
        total_votes +=1

       #Print the candidate name from each row
        candidate_name=row[2]
        #If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            #Add it to the list
            candidate_options.append(candidate_name)
            #Begin tracking vote count
            candidate_votes[candidate_name]=0
        candidate_votes[candidate_name] +=1
       


#Determine percentage of votes
#Iterate through the candidate list
for candidate_name in candidate_votes:
    #Candidate vote count
    votes = candidate_votes[candidate_name]
    #Calculate percentage
    vote_percentage=float(votes)/float(total_votes) *100
    
    #Determine winning vote count and candidate
    #Are votes greater than winning count?
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage=vote_percentage
        winning_candidate=candidate_name

    #Print it fancy
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
winning_candidate_summary = (f"------------------------\n"
                                f"Winner:  {winning_candidate}\n"
                                f"Winning Vote Count:  {winning_count:,}\n"
                                f"Winning Percentage: {winning_percentage:.1f}%\n"
                                f"-------------------------\n")
print(winning_candidate_summary)