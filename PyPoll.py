# Add our dependencies
import csv
import os
# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join('analysis', "election_analysis.txt")

# Initalize a total vote count
total_votes = 0

# Candidate options
candidate_options = []

# Declare the empty dictionary
candidate_votes = {}

# Winning Candidate, Winning Percentage, and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#  Open the election results and read the file
with open(file_to_load) as election_data:
    
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)

    # Print each row in the CSV file
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]

        # Add unique candidate name to the candidate list
        if candidate_name not in candidate_options:
            # Add to the list
            candidate_options.append(candidate_name)

            # Begin tracking the candidate's vote count
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

    # Save the results to our text file
with open(file_to_save, 'w') as txt_file:

    # Print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"-----------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-----------------------\n"
    )
    print(election_results, end="")
    # Save the final vote coint to the text file
    txt_file.write(election_results)
    
    # Determine the percentage of votes for each candidate
    # Iterate through candidate list
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes
        vote_percentage = float(votes)/float(total_votes)*100
        
        # To do: print out each candidate's name, vote count, and percentage of votes to the terminal
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
        #Print the results for each cadidate
        print(candidate_results)
        # Save the candidate results to our text & terminal
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent = vote_percentage 
            # winning_candidate = candidate_name
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
            
        # To do: print out the winning candidate, vote count, and percentage to terminal
    winning_candidate_summary = (
        f"--------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"--------------------------\n")
    print(winning_candidate_summary)

    # Save the candidate's results to the text file
    txt_file.write(winning_candidate_summary)

   
        

