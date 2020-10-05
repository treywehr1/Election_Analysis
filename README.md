# Election_Analysis

## Election Audit: Purpose
This election audit was conducted in order to ensure accurate and satisfactory results be submitted to the Colorado Board of Elections for their recent election cycle. Python was used to properly ingest and manipulate the provided election data so that it be accurately and easily analyzed. Results were submitted in .txt format.

## Election Audit Results
 - In total, 369,711 votes were cast.
 
 - In terms of number of votes and percentage of total votes across all 3 applicable precinct counties...
    1. Jefferson Co. had 10.5% of votes, or 38,885 total votes
    2. Denver Co. had 82.8% of votes, or 306,055 total votes 
    3. Arapahoe Co. had 6.7% of votes, or 24,801 total votes
  
 - Denver Co. had the largest voter turnout. (306,055 voters)
 
 - In terms of number of votes and percentage of total votes across all 3 applicable election candidates...
    1. Charles Casper Stockham won 23% of votes, or 85,213 total votes
    2. Diana DeGette won 73.8% of votes, or 272,892 total votes
    3. Raymon Anthony Doane won 3.1% of votes, or 11,606 total votes

 - Diana DeGette won the the precinct with 73.8% of votes, or 272,892 total votes.
 
## Audit Summary 

This python script can be used, with some modification, for any election. This relies mostly on the format of provided data. Should the election result data, in .csv format, maintain it's current format, of candidate's names in column 3, and county name in column 2 - then you can run this script unchanged. However, so long as you import a .csv and know what columns your county names falls within, and which column your candidate's names fall within - you can use said column's index number to very minimally alter the script to work with your data. In example, if your candidate name was in column 5 and your county name fell within column 4 - you would simply change the number in parenthesis in the below script to those column's corresponding index number (column # - 1).

![Imgur](https://imgur.com/BylvQ6w.png)

So, your two options to get this script to work with any .csv of data would be to
  
  - Re-position candidate names and county names to columns 3 and 2 respectively.
  - Ammend the below section of script to fit the candidate names and county names column's corresponding index number.
  
With this script and additional formatting information provided above, this script will prove to be effective in providing it's election analysis.


