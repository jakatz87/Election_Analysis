# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies so we can read the file we are using
# with Python commands.
import csv
import os

# Add a variable to load the file from the path on your computer.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path, using a diferent folder.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter, so this is better than counting all the rows.
total_votes = 0

# Creat Candidate Options as a list and candidate votes as a dictionary.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
county_list=[]
county_votes={}

# Track the winning candidate,  initialize a vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and initialize county voter turnout and percentage.
county_largest=""
county_turnout=0
county_percentage=0

# Read the csv and convert it into a list of dictionaries with a new variable.
# The work is done within this With Open statement
with open(file_to_load) as election_data:
    # Note the language used from the dependencies. We'll create another new variable.
    reader = csv.reader(election_data)

    # Read the header so the top row of the csv is excluded from the vote count.
    header = next(reader)

    # This for loop will count the total votes for each row (new variable) in the CSV file.
    for row in reader:

        # Add to the total vote count, based on what we initialized earlier.
        total_votes = total_votes + 1

        # Get the candidate name (new variable) from each row. Remember indexing starts at 0.
        candidate_name = row[2]

        # 3: Extract the county name (new variable) from each row.
        county_name=row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list we set up earlier.  
        # This will print each name only once.
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count for the 
            # dictionary we created earlier.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count. This puts the vote total
        # for each candidate in this dictionary with the name.
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_list:

            # 4b: Add the existing county to the list of counties.
            county_list.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name]=0

        # 5: Add a vote to that county's vote count in the county dictionary.
        county_votes[county_name] +=1


# Save the results to our text file.  Notice we are using the file to 
# save variable from the beginning.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Print this on the txt file as well.
    txt_file.write(election_results)
    
    # 6a: Write a for loop to get the county name (new variable) from the county dictionary.
    for county_name in county_votes:
        # 6b: Retrieve the county vote count (new variable).
        cvotes=county_votes.get(county_name)
        # 6c: Calculate the percentage of votes for the county.
        cvote_percentage=float(cvotes)/float(total_votes)*100
         # 6d: Print the county results to the terminal.
        county_results = (
            f"{county_name}: {cvote_percentage: .1f}% ({cvotes:,})\n")
        print(county_results)
         # 6e: Print the county votes on the text file.
        txt_file.write(county_results)
         # 6f: Write an if statement to determine the largest voting county 
         # and get its vote count.
        if (cvotes > county_turnout): #this changes cvotes for the first name.
            county_turnout = cvotes  #then it holds that value for the loop until
                                    # it is met again, if ever.
            county_largest = county_name  #the highest cvote count in the dictionary
                                            # is linked to the name.
            
    # 7: Print the county with the largest turnout to the terminal.
    largest_county_summary = (
        f"-------------------------\n"
        f"Largest County Turnout: {county_largest}\n"
        f"-------------------------\n")
    print(largest_county_summary)

    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(largest_county_summary)

    # Save the final candidate vote count to the text file.
    # Create a nice  header
    candidate_header=("\n"
        f"Candidate Results\n"
        f"-------------------------\n")
    print(candidate_header)
    txt_file.write(candidate_header)
    
    #Create conditions to calculate cadidate results with the 
    # candidate name variable using the candidate votes dictionary.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
