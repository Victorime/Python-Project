import os

# Module for reading CSV files
import csv
from statistics import mean
csvpath = os.path.join('.', 'Resources', 'election_data.csv')
outputpath = os.path.join('.', 'Output', 'Election_Data_Analysis_Summary.txt')
VoterList =[]
CountryList =[]
CandidateList= []
Candidates = []
CandidateVotes= []
CandidateVotePercentage= []
with open(csvpath, newline='', encoding="utf-8") as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
	csvreader = csv.reader(csvfile, delimiter=',')
	csv_header = next(csvreader)

	for row in csvreader:
		VoterList.append(row[0])
		CountryList.append(row[1])
		CandidateList.append(row[2])