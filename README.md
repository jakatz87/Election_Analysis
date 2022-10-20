# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

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

## Results

![image](https://github.com/jakatz87/Election_Analysis/blob/main/Resources/Results%20Screenshot.png)

## Summary
For this project I learned how to load, read, and write to a CSV file with:
```
import csv
import os

# Create the variable and use the path to the location of the CSV file.
file_to_load = os.path.join("Resources", "election_results.csv")

# Create the variable and use the path to the location of the future text file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# When it's time to write the code commands, begin reading (by default) the with-open code
with open(file_to_load) as election_data:

# When it's time to write the coding results to a text file, use the with-open code with the "w"rite command
with open(file_to_save, "w") as txt_file:
```

