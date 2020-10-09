# Election_Analysis

## Election Audit Overview
A colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election. 

1. Calculate the total number of votes cast. 
2. Get a complete list of candidates who recieved votes.
3. Calculate the percentage of votes each candidate won.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.
6. Determine the county with the largest voter turnout 

## Resources 
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code 1.50.0

## Election Audit Overview
For this challenge, the dataset election_results is given by the Colorado Board of Elections to tabulate the total number of votes cast, the candidates names and their correlating number of votes cast for them, as well as the percentage of votes that each candidate recieved. From these we are able to obtain the projected winner of the election based on popular votes as well as the percent of votes the winner recieved. We also were requested to find the county with the largest voter turn out thus we analyzed the data to find the county with the largest voter turnout and their correlating vote percentage as well as total number of votes in that county.
  
## Election Audit Results 
![election_analysis](analysis/election_analysis.txt)

The analysis of the election shows that:

- There were 369,711 votes cast in the congression election.

- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane

- The candidate results were
  - Charles Casper Stockham recieved 23% of the votes and 85,213 number of votes
  - Diana DeGette recieved 73.8% of the votes and 272,892 number of votes
  - Raymon Anthony Doane recieved 3.1% of the votes and 11,606 number of votes

- The Colorado counties in this precinct results were
    - Jefferson recieved 10.5% of the cotes and 38,855 number of votes
    - Denver recieved 82.8% of the votes with 306,055 number of votes
    - Arapahoe recieved 6.7& of the votes with 24,801 number of votes 
 
- The winnner of the election was:
  - Diana DeGette, who recieved 73.8% of the votes and 272,892 number of votes

- The county with the largest voter turnout was:
    - Denver, who recieved 82.8% of the votes and 306,055 number of votes 

## Election Audit Summary
This script can be used to examine an election csv file. To use for a different data source importing the correcr csv file instead of the colorado election results csv file can let you perform this analysis on that particular data set. Adjusting iterations through the rows in order to extract the correct data will depend on the csv file you embed into the analysis - in this case the candidate names are in the second row and the counties are in the first row, as displayed in the script for this analysis. Making sure youre iterating through the correct row will make an analysis available for any election results data. 


 
 
  
  
  

