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

# Open the election results and read the file.
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)
# Read and print the header row.    
    headers = next(file_reader)
    print(headers)

    # To do: Perform analysis


# Using the with statement open the file as a text file.
with open(file_to_save, 'w') as txt_file:
    # Write some data to the file.
    txt_file.write("Counties in the election\n-------------------\nArapahoe\nDenver\nJefferson")

