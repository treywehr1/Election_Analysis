# Data needed to retrieve
    # 1. Total number of votes cast
    # 2. Candidates who received votes
    # 3. total number of votes each candidate received
    # 4. oercentage of vote each candidate won
    # 5. winner based on popular vote
# Add dependencies
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "resource_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0
candidate_options = [] 
# declare and empty dictionary
candidate_votes = {}

winning_candidate = " "
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)
# Read and print the header row.    
    headers = next(file_reader)
    print(headers)

    # To do: Perform analysis
    for row in file_reader:
        # 2. Add to the total vote count
        total_votes += 1
        # print candidate name from each row
        candidate_name = row[2]

        if candidate_name not in candidate_options:
        # add candidate name to candidate list
            candidate_options.append(candidate_name)

            # Begin tracking that candidates vote count 
            candidate_votes[candidate_name] = 0
            # add a vote to candidate's count
        candidate_votes[candidate_name] += 1

    for candidate_name in candidate_votes:
        
        # 2. retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        
    #  To do: print out each candidate's name, vote count, and percentage of votes to the terminal.
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.

        if (votes > winning_count) and (vote_percentage > winning_percentage):
        # 2. If true then set winning_count = votes and winning_percent = vote_percentage.  
            winning_count = votes
            winning_percentage = vote_percentage
            # 3. Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

    #  To do: print out the winning candidate, vote count and percentage to terminal.

    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    
print(winning_candidate_summary)

print(candidate_votes)


    

# # Using the with statement open the file as a text file.
# with open(file_to_save, 'w') as txt_file:
#     # Write some data to the file.
#     txt_file.write("Counties in the election\n-------------------\nArapahoe\nDenver\nJefferson")

