# Election Audit

## Overview of Project

This project consists of analyzing election data for counties and candidates in understanding their total number of votes, percentage of voters, and overall candidate and county winners.

### Purpose

The purpose of this project is to learn how to use python to analyze election data from a CSV file. This project involves doing the following:

1. Reading the CSV file from a particular folder.
2. Initializing objects.
3. Creating dictionaries, lists and variables.
4. Creating for-loops for iterating through rows of the data.
5. Print to terminal and save election results into a new txt file.

## Election Audit Results

### Summary of Analysis Steps

- Initatize dictionary and lists.
- Initialize value and string objects.
- Read the election results file
- Find the headers
- Find the names of the candidates and counties of each row.
    - Add the candidate name to the candidate list
        - Then begin tracking the candidate voter count
    - Add the county to the county list
        - Then begin tracking the candidate voter count  
    - Save the results of the total votes to the text file and print to the terminal. 
    - The output should look like this:
![Total voting Result](https://github.com/jennymvo/Election_Analysis/blob/main/images/Screen%20Shot%202022-09-28%20at%2011.43.42%20AM.png?raw=true)
- Create a for-loop for finding the county vote count, and find the percentage of the votes for each county.
- Find the winning county by finding the county with the largest vote count
    - Print the results to the terminal and save results into the text file
    - The output should look like this:
![County Votes](https://github.com/jennymvo/Election_Analysis/blob/main/images/county_votes.png?raw=true)
- Find the largest county turnout by writing an if statement for the county with the highest vote count and the highest voting percentage.
- The output should look like this:
![Largest County Turnout](https://github.com/jennymvo/Election_Analysis/blob/main/images/largest_county_turnout.png?raw=true)
- Retrieve the vote count and the percentage of candidate votes.
    - Print the results for each candidate and save the results to the text file.
- The output should look like this:
![Results of the voting distribution for candidates](https://github.com/jennymvo/Election_Analysis/blob/main/images/candidates.png?raw=true)
- Find the winning candidate by finding the candidate with the highest number of votes and highest percentage of votes.
    - Print the results of the winning candidate and save to the text file.
- The output should look like this:
![Winning Candidate Results](https://github.com/jennymvo/Election_Analysis/blob/main/images/winningcandidate.png?raw=true)

## Election Audit Summary

###### There is a statement to the election commission that explores how this script can be used for any election, with two examples for modifying the script

This script automates the analysis of the county and candidate elections from an input file containing all the data. 

This script can be used for any election, as long as the input file as long as each row represents one vote, and the information is organized with the information in their respective columns. Depending on where the candidate and area of votes are organized on the sheet, the column data that is being extracted can be modified easily from rows 50 and 53 in the script by changing it to the row of interest. 

Another way this script can be modified is by looking for the losers of the election to be able to publically shame them by adding lines like so:

```python
lowestCounty = min(countyVotes.values())
LoserCounty = [k for k, v in countyVotes.items() if v==lowestCounty]
print(f" The county with the lowest voter turnout is {LoserCounty} with only {min(countyVotes.values())} votes")
```

This can also be modified to find the loser candidate:

```python
lowestCandidate = min(candidate_votes.values())
LoserCandidate = [k for k, v in candidate_votes.items() if v==lowestCandidate]
print(f" The loser candidate is {LoserCandidate} with only {min(candidate_votes.values())} votes")
```
