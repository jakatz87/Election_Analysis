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

#Create a filename variable to a direct or indirect path to the file.
file_to_save=os.path.join("analysis", "election_analysis.txt")

#Open the election results and read the file
with open(file_to_load) as election_data:
    # Read and analyze the data here.
    file_reader=csv.reader(election_data)

    #Print the header row
    headers=next(file_reader)
    print(headers)
