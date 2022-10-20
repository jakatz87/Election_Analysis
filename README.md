# Election Analysis

## Project Overview
A Colorado Board of Elections employee has given me the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who recieved votes.
3. Provide a breakdown of the number of votes and percentage of votes by county.
4. Show which county had the largest number of votes.
5. Calculate the total number of votes each candidate recieved.
6. Calculate the percentage of votes each candidate won.
7. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code

## Process
For this project I had to load, read, and write to a CSV file with:

```
import csv
import os
```
```
# Create the variable and use the path to the location of the CSV file.
file_to_load = os.path.join("Resources", "election_results.csv")
```
```
# Create the variable and use the path to the location of the future text file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
```
```
# When it's time to write the code commands, begin reading (by default) the with-open code
with open(file_to_load) as election_data:
```
```
# When it's time to write the coding results to a text file, use the with-open code with the "w"rite command
with open(file_to_save, "w") as txt_file:
```
When reading the CSV file, after `with open(file_to_load) as election_data:`, I had to use the correct dependency language of `reader=csv.reader(election_data)` to make the "reader" variable.  Now the program can exclude the header data in the file so it's not counted with the data:  `header = next(reader)`.

The first "for" loop begins to count total votes, candidate names, and county names
```
 for row in reader:

        # Add to the total vote count, based on what we initialized earlier.
        total_votes = total_votes + 1

        # Get the candidate name (new variable) from each row. Remember indexing starts at 0.
        candidate_name = row[2]

        # Extract the county name (new variable) from each row.
        county_name=row[1]
```
In order to display the vote counts so that each candidate name and each county name is shown once, I use empty lists and dictionaries that were created before the "for" loop was opened:
```
candidate_options = []
candidate_votes = {}

county_list=[]
county_votes={}
```
Inside the "for" loop, I can now read the proper information and place it into the proper list and dictionarry:
```
        # If the candidate does not match any existing candidate add it to the candidate list we set up earlier. This will print each name only once.
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count for the dictionary we created earlier.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count. This puts the vote total for each candidate in this dictionary with the name.
        candidate_votes[candidate_name] += 1

        # Write an if statement that checks that the county does not match any existing county in the county list.
        if county_name not in county_list:

            # Add the existing county to the list of counties.
            county_list.append(county_name)

            # Begin tracking the county's vote count.
            county_votes[county_name]=0

        # Add a vote to that county's vote count in the county dictionary.
        county_votes[county_name] +=1
```
I have now read everything I need from the CSV file.  It is time to display the information I want to see by writing and printing.
I begin with the overall results:
```
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
    # I placed the "County Votes" header here because it is outside the "for" loop necessary for those results.
    # Print this on the txt file as well.
    txt_file.write(election_results)
```
The printed results on the text file will look like:

![image](https://github.com/jakatz87/Election_Analysis/blob/main/Resources/General%20Results%20Header.png)


I create a "for" loop to get each county's results and print them:
```
 for county_name in county_votes:
        # Retrieve the county vote count (new variable).
        cvotes=county_votes.get(county_name)
        # Calculate the percentage of votes for the county.
        cvote_percentage=float(cvotes)/float(total_votes)*100
         # Print the county results to the terminal.
        county_results = (f"{county_name}: {cvote_percentage: .1f}% ({cvotes:,})\n")
        print(county_results)
         # Print the county votes on the text file.
        txt_file.write(county_results)
```
Inside that "for" loop, I find which county has the highest turnout depending on "if" the votes in the list by county `cvotes` are higher than the previous county total, `county_turnout`, which was set to 0 when initialzed.  By default, the first county read will be have the highest turnout, then that amount will be the comparitive value for the next iteration in the loop.  The county with the highest turnout will remain until a `cvotes` amount is greater and becomes the new comparitive amount.
```
# Write an if statement to determine the largest voting county and get its vote count.
        if (cvotes > county_turnout): #this changes cvotes for the first name.
            county_turnout = cvotes  #then it holds that value for the loop until it is met again, if ever.
            county_largest = county_name  #the highest cvote count in the dictionary is linked to the name.
 ```
 I can now print the results:
 ```
  # Print the county with the largest turnout to the terminal.
    largest_county_summary = (
        f"-------------------------\n"
        f"Largest County Turnout: {county_largest}\n"
        f"-------------------------\n")
    print(largest_county_summary)

    # Save the county with the largest turnout to a text file.
    txt_file.write(largest_county_summary)
```
The printed results on the text file will look like:

![image](https://github.com/jakatz87/Election_Analysis/blob/main/Resources/County%20Turnout%20Print%20Results.png)


I now create another separate "for" loop to repeat the process to print the candidate results and winner.
First, the header for the text file:
```
 candidate_header=("\n"
        f"Candidate Results\n"
        f"-------------------------\n")
    print(candidate_header) # for the terminal
    txt_file.write(candidate_header) # for the text file
```
The "for" loop with the candidate results, found in the lists and dictionaries we created and read:
```
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        print(candidate_results) # for the terminal
        txt_file.write(candidate_results) # for the text file
```
The process to determine the winner, by vote and percentage, is the same as the process for the largest county: holding the count of the `votes` variable in the loop if a candidate's results are greater.
```
 if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate and using a visually appealing format
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
```
The printed results on the text file will look like:

![image](https://github.com/jakatz87/Election_Analysis/blob/main/Resources/Candidate%20Print%20Results.png)


## Results and Summary
The formatting I used in the code will allow us to clearly see all the information requested by the Board of Elections.

![image](https://github.com/jakatz87/Election_Analysis/blob/main/Resources/Results%20Screenshot.png)

Congratulations Diana!
